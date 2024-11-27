from extract_data_pdf_process import ExtractDataPdfProcess
from econodata import Econodata
from dotenv import load_dotenv
import time
import sys

load_dotenv()

filename = sys.argv[1]
count_threads = sys.argv[2]
# Econodata().pesquisar_pela_razao_social("EMPRESA LTDA")
ExtractDataPdfProcess(filename, count_threads).run()
