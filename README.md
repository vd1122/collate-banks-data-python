This tool is based on the exercise given at the link -
https://gist.github.com/Attumm/3927bfab39b32d401dc0a4ca8db995bd

```
This tool collates accounting data received from different bank. 

The bank's data file could be in different format (e.g. csv, json, xml) with different headers order.
Also data in the bank's file could be in different format.

This tool is extendable for new banks/file types/data formats.
```

Below sections cover information about -
```
1. Script run
2. Script output (./data/output-data-files/accounting.csv)
3. Log output
4. Tests run
5. Tests Log Output
6. Project directory structure
``` 

> Script Run
```
python accounting.py
```
> Script output
```
Bank,Date,Type,Amount,From,To
Bank1,01 Oct 2019,remove,99.20,198,182
Bank1,02 Oct 2019,add,2000.10,188,198
Bank2,03 Oct 2019,remove,99.40,198,182
Bank2,04 Oct 2019,add,2123.50,188,198
Bank3,05 Oct 2019,remove,5.70,198,182
Bank3,06 Oct 2019,add,1060.80,188,198
```
> Log Output
```
2021-03-25 01:50:05,315 -            utils.config -    INFO - Config file: /home/vikas/myrepo/python-test/config.ini
2021-03-25 01:50:05,317 -            utils.config -   DEBUG - Config settings for INPUT:DATA-DIR is data/input-data-files
2021-03-25 01:50:05,317 -            utils.config -   DEBUG - Config settings for OUTPUT:DATA-FILE is data/output-data-files/accounting.csv
2021-03-25 01:50:05,317 -            utils.config -   DEBUG - Config settings for OUTPUT:FILE-FORMAT is csv
2021-03-25 01:50:05,318 -            utils.config -   DEBUG - Config settings for ACCOUNTING:BANKS-LIST is Bank1,Bank2,Bank3
2021-03-25 01:50:05,318 -      modules.accounting -    INFO - Collating bank data
2021-03-25 01:50:05,318 -         factories.banks -   DEBUG - Returning bank [Bank1] object
2021-03-25 01:50:05,319 -            utils.config -   DEBUG - Config settings for INPUT DATA FILENAME:Bank1 is bank1.csv
2021-03-25 01:50:05,319 -      modules.accounting -    INFO - Processing [Bank1] input data file [data/input-data-files/bank1.csv]
2021-03-25 01:50:05,319 -  factories.file_readers -   DEBUG - Returning [csv] reader object
2021-03-25 01:50:05,326 -    modules.file_readers -    INFO - Reading CSV input file: data/input-data-files/bank1.csv
2021-03-25 01:50:05,333 -         factories.banks -   DEBUG - Returning bank [Bank2] object
2021-03-25 01:50:05,334 -            utils.config -   DEBUG - Config settings for INPUT DATA FILENAME:Bank2 is bank2.csv
2021-03-25 01:50:05,334 -      modules.accounting -    INFO - Processing [Bank2] input data file [data/input-data-files/bank2.csv]
2021-03-25 01:50:05,334 -  factories.file_readers -   DEBUG - Returning [csv] reader object
2021-03-25 01:50:05,334 -    modules.file_readers -    INFO - Reading CSV input file: data/input-data-files/bank2.csv
2021-03-25 01:50:05,336 -         factories.banks -   DEBUG - Returning bank [Bank3] object
2021-03-25 01:50:05,336 -            utils.config -   DEBUG - Config settings for INPUT DATA FILENAME:Bank3 is bank3.csv
2021-03-25 01:50:05,336 -      modules.accounting -    INFO - Processing [Bank3] input data file [data/input-data-files/bank3.csv]
2021-03-25 01:50:05,337 -  factories.file_readers -   DEBUG - Returning [csv] reader object
2021-03-25 01:50:05,337 -    modules.file_readers -    INFO - Reading CSV input file: data/input-data-files/bank3.csv
2021-03-25 01:50:05,338 -  factories.file_writers -   DEBUG - Returning [csv] writer object
2021-03-25 01:50:05,339 -    modules.file_writers -    INFO - Writing to CSV file: data/output-data-files/accounting.csv
2021-03-25 01:50:05,339 -      modules.accounting -    INFO - Process over
```

> Tests Run
```
cd ./tests
python run_all_tests.py
```

> Tests Log Output
```
======================================================================
Executing test script [test_banks_instances.py]
======================================================================
test_bank1_csv_output_line (__main__.TestBankInstance) ... ok
test_bank2_csv_output_line (__main__.TestBankInstance) ... ok
test_bank3_csv_output_line (__main__.TestBankInstance) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.009s

OK
======================================================================
Executing test script [test_file_readers_instances.py]
======================================================================
test_csv_file_reader (__main__.TestFileReaders)
Steps: ... skipped 'TODO'
test_json_file_reader (__main__.TestFileReaders)
Steps: ... skipped 'TODO'

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK (skipped=2)
======================================================================
Executing test script [test_file_writer_factories.py]
======================================================================
test_file_writers_factory (__main__.TestFileWritersFactory) ... ok
test_file_writers_factory_exception (__main__.TestFileWritersFactory) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
======================================================================
Executing test script [test_file_writers_instances.py]
======================================================================
test_csv_file_writer (__main__.TestFileWriters)
Steps: ... skipped 'TODO'
test_json_file_writer (__main__.TestFileWriters)
Steps: ... skipped 'TODO'

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK (skipped=2)
======================================================================
Executing test script [test_bank_factories.py]
======================================================================
test_banks_factory (__main__.TestBanksFactory) ... ok
test_banks_factory_exception (__main__.TestBanksFactory) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
======================================================================
Executing test script [test_file_reader_factories.py]
======================================================================
test_file_readers_factory (__main__.TestFileReadersFactory) ... ok
test_file_readers_factory_exception (__main__.TestFileReadersFactory) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s
```

> Project Directory Structure -
```.
├── README.md
├── accounting.py
├── config.ini
├── data
│   ├── input-data-files
│   │   ├── bank1.csv
│   │   ├── bank2.csv
│   │   └── bank3.csv
│   └── output-data-files
│       └── accounting.csv
├── lib
│   ├── __init__.py
│   ├── factories
│   │   ├── banks.py
│   │   ├── file_readers.py
│   │   └── file_writers.py
│   ├── modules
│   │   ├── accounting.py
│   │   ├── banks.py
│   │   ├── file_readers.py
│   │   └── file_writers.py
│   └── utils
│       ├── config.py
│       ├── exceptions.py
│       └── log.py
└── tests
    ├── run_all_tests.py
    ├── test_bank_factories.py
    ├── test_banks_instances.py
    ├── test_file_reader_factories.py
    ├── test_file_readers_instances.py
    ├── test_file_writer_factories.py
    └── test_file_writers_instances.py
```
