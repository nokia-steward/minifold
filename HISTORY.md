## 0.0.1 (2018-08-29): First release

* Initial commit

## 0.10.0 (2023-04-15)

* Migrated to poetry
* Enabled CI

## 0.10.1 (2025-03-10)

* Documentation:
  * Migrated to `pydata` theme.
  * Updated installation steps.
* Package:
  * Exposed `DEFAULT_CACHE_STORAGE_BASE_DIR`, `make_cache_dir`.
  * Updated `AUTHORS.md` and `HISTORY.md`.
* `DblpConnector`:
  * Improved `DocType` handling.
  * Implemented timer to mitigate rate limitation queries.
  * Fixed URL when data is fetched through the XML API.
* Bug fix:
  * Fixed `DocType.__str__`.
  * Fixed `Query.__str__`.
* Improved tests to be more robust to network failures:
  * `GoogleScholarConnector`.
  * `HalConnector`.

## 0.10.2 (2025-03-10)

* Documentation:
  * Improved documentation template.
* Improved code quality (`flake8`).
* Project:
  * Improved `setup.cfg`.
  * Improved `Makefile`.

## 0.10.2 (2025-05-27)

* Fixed documentation build (readthedoc).

## 0.10.3 (2026-10-22)

* Updated DBLP connector to cope with Anubis firewall.
