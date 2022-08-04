Change Log
==========

1.1.4 (2022-08-04)
------------------

* Add new check DJ13, ensures the receiver decorator is at the top of the
  decorators list.

1.1.3 (2022-08-04)
------------------

* Add compatibility with flake8 4.x (@terencehonles)

1.1.2 (2021-05-11)
------------------

**Bugfixes**

* Removed UUIDField from DJ01 (@noamkush)
* Removed ImageField from DJ01 (Ferran Jovel)

**Improvements**

* Re-add `DJ10` and `DJ11` (verbose_name and verbose_name_plural checks) as optional checks which are disabled by default (@rocioar)
* Update DJ12 error message (@sondrelg)

1.1.1 (2020-05-25)
------------------

**Bugfixes**
* Fixed bug on `DJ01` when the keyword argument value of `unique`, `blank` or `null` keywords was not a simple value.

1.1.0 (2020-05-24)
------------------

**Bugfixes**

* Fixed `DJ01` to consider exception when unique=True and null=True warning should not be raised. (@rocioar)

**Improvements**

* Added documentation for all the Rules. (@rocioar)
* Removed `DJ09`, `DJ10` and `DJ11` since it should not be mandatory to set a `verbose_name` or `verbose_name_plural`. (@rocioar)
* Removed `DJ05` check since we don't have a way to now when namespaces could be skipped (@rocioar)
* Re-wrote Rules description for better understanding. (@rocioar)

1.0.0 (2020-04-16)
------------------

**Bugfixes**

* Bug fix for RenderChecker (@GitRon)

**Improvements**

* Removed `DJ04` check since Django uses dashes on their examples (@rocioar)
* Removed `DJ02` since it's not applicable anymore. Django has deprecated NullBooleanField. (@rocioar)
* Added Model Content Order Check `DJ12`. (@denizdogan)
* Removed tox, use Github Actions for running tests and coverage (@rocioar)
* Dropped support for Python 3.4 (@rocioar)


0.0.5 (2019-05-06)
------------------

**Improvements**

- Changed `DJ08` check for `__str__` method to ignore abstract models (@denizdogan)
- Added `DJ09` - Model must define `class Meta`  (@avallbona)
- Added `DJ10` - Class Meta from Model has to define `verbose_name`  (@avallbona)
- Added `DJ11` - Class Meta from Model has to define `verbose_name_plural`  (@avallbona)
- Fixed some flake8 issues in test files (@avallbona)
- Refactored some tests  (@avallbona)

0.0.4 (2019-01-18)
------------------

**Improvements**

- Added `DJ06` check for ModelForm, should not use exclude (@rocioar)
- Added `DJ07` check for `ModelForm.META`, should not set fields to `'__all__'` (@rocioar)
- Added `DJ08` check for Model, should contain `__str__` method (@rodolfolottin)

0.0.3 (2018-10-03)
------------------

**Bugfixes**

- Fixed bug in setup.py missing some modules (@lithammer)

0.0.2 (2018-10-02)
------------------

**Bugfixes**

- Fixed bug in `ModelFieldChecker` where node is not one of Name or Attribute (@rocioar)

**Improvements**

- Added checks `DJ04` and `DJ05` for urls (@rocioar)
- Reorganized code, moved individual checkers to `checkers/`, `tests to tests/` (@rocioar)
- Added coverage checks (@rocioar)
- Moved from Travis to CircleCI (@rocioar)


0.0.1 (2018-09-28)
------------------

Initial version
