from faker import Faker
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
import random
from time import time
import os
from dotenv import load_dotenv

load_dotenv()
faker = Faker("ko-KR")


engine = create_engine(
    f'mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_TEST_PART1_NAME")}'
)
metadata = MetaData()
your_table = Table("post", metadata, autoload_with=engine)
for i in range(30):
    Session = sessionmaker(bind=engine)
    session = Session()

    data_start = time()
    data = [
        {
            "memberId": random.randint(1, 10),
            "content": faker.catch_phrase(),
            "created_at": faker.date_this_century(),
            "updated_at": faker.date_this_century(),
        }
        for _ in range(100000)
    ]
    print(f"Data 생성 시간 : {time()-data_start}")

    insert_start = time()
    insert_stmt = your_table.insert().values(data)
    session.execute(insert_stmt)
    print(f"Data 주입 시간 : {time()-insert_start}")

    session.commit()

    print(f"{i+1} 번 째 주입 완료")
