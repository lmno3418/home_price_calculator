Structure planned
```
home_price_calculator/
│── src/
│   ├── main/
│   │   ├── models/
│   │   │   ├── person.py
│   │   │   ├── labour.py
│   │   │   ├── mistri.py
│   │   │   ├── homebuyer.py
│   │   ├── databases/
│   │   │   ├── mysql_connector.py
│   │   ├── factories/
│   │   │   ├── person_factory.py
│   │   ├── services/
│   │   │   ├── labour_service.py
│   │   │   ├── attendance_service.py
│   │   ├── utility/
│   │   │   ├── encrypt_decrypt.py
│   │   ├── main.py
│── resources/
│   ├── config/
│   │   ├── config_file.ini
│   │   ├── db_script.sql
│── tests/
│   ├── test_labour.py
│   ├── test_mistri.py
│   ├── test_homebuyer.py
│── requirements.txt
│── README.md
