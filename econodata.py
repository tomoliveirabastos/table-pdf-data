import requests
import json
from typing import List
from models.Company import Company
from sqlalchemy import select
from db_engine import get_engine_session
import re
from os import environ

class Econodata:
    def __init__(self):
        self.token = environ['ECONODATA_TOKEN']
        self.base_url = "www.econodata.com.br"

    def pesquisar_pela_razao_social(self, nome_razao_social: str) -> List[Company]: 
        url = "https://www.econodata.com.br/gateway/ecdt-busca/searchCompaniesSite"

        payload = json.dumps({
            "input": nome_razao_social
        })
    
        headers = {
            'User-Agent': '*/*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'Cookie': environ['COOKIE_TOKEN']
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        j = json.loads(response.text)

        engine, session = get_engine_session()
        Company.metadata.create_all(engine)

        companies = []

        for company in j['companies']:
            company["cd_cnpj"] = re.sub("[^a-zA-Z0-9]", "", company["cd_cnpj"])

            c = Company(**company)

            rows = session.execute(select(Company).where(Company.cd_cnpj == company["cd_cnpj"])).all()

            if len(rows) == 0:
                session.add(c)
                companies.append(c)

        session.commit()

        return companies