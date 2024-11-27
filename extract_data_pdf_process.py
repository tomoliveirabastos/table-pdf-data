import camelot
import PyPDF2
import threading
import queue
from multiprocessing import Pool
from econodata import Econodata
import time

class ExtractDataPdfProcess:
    def __init__(self, file_path, position_column_number):
        self.file_path = file_path
        self.position_column_number = position_column_number
        self.pdf_reader = PyPDF2.PdfReader(self.file_path)
        self.number_pages = len(self.pdf_reader.pages)

    def worker(self, worker, page):
        while True:
            nome_razao_social = worker.get()
            print('pesquisando na econodata', nome_razao_social)
            
            Econodata().pesquisar_pela_razao_social(nome_razao_social)
            time.sleep(3)

            print('terminou de pesquisar', nome_razao_social)
            worker.task_done()

    def handle_process(self, page_number):
        print('iniciado pagina', page_number)
        q = queue.Queue()
        threading.Thread(target=self.worker, daemon=True, args=[q, page_number]).start()

        table = self.parse_table_pdf(page_number, q)

        q.join()

        return table

    def parse_table_pdf(self, page_number, worker_queue):
        file_pdf_camelot = camelot.read_pdf(self.file_path, pages=str(page_number))

        list_rows = []

        for a in file_pdf_camelot:

            rows = a.df[self.position_column_number - 1].values.tolist()

            for nome_razao_social in rows:
                list_rows.append(nome_razao_social)
                if nome_razao_social.strip() != "" and nome_razao_social != None:
                    worker_queue.put(nome_razao_social.strip())
                    # print(nome_razao_social.strip())

        return list_rows

    def run(self):
        list_params = []

        for number in range(1, self.number_pages + 1):
            list_params.append(number)

        p = Pool()
        list_rows = p.map(self.handle_process, list_params)
        return list_rows