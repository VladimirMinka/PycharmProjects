import pytest
class TestCase:
    __test__ = False

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name
        self._status = "Untested"

    def __str__(self):
        return f"[ID: {self.tc_id}] {self.name} - Статус: {self._status}"

    def __eq__(self, other):
        if isinstance(other, TestCase):
            return self.tc_id == other.tc_id
        return NotImplemented

    def run_case(self):
        raise NotImplementedError(f"{self.tc_id} {self.name} Статус{self._status}")

    def get_status(self):
        return self._status

    def set_status(self, status):
        is_valid = ["Untested", "Passed", "Failed", "Skipped"]
        if status not in is_valid: raise ValueError("Недопустимый статус")
        self._status = status


class ManualTestCase(TestCase):
    def __init__(self, tc_id, name, tester_name):
        super().__init__(tc_id, name)
        self.tester_name = tester_name

    def run_case(self):
        return f"Ручное прохождение теста {self.name} тестировщиком {self.tester_name}"


class AutomatedTestCase(TestCase):
    def __init__(self, tc_id, name, browser, environment):
        super().__init__(tc_id, name)
        self.browser = browser
        self.environment = environment

    def run_case(self):
        return f"Запуск автотеста {self.name} в браузере {self.browser} на стенде {self.environment}"

def test_str():
    ts = TestCase(1, "vlad123")
    assert str(ts) == "[ID: 1] vlad123 - Статус: Untested"

def test_set_status():
    ts1 = TestCase(2, "serg 456")
    ts1.set_status("Passed")
    assert ts1.get_status() == "Passed"
def test_set_invalid_status():
    ts2 = TestCase(3, "igor 789")
    with pytest.raises(ValueError):
        ts2.set_status("Error")
def test_eq():
    ts3= TestCase(1, "vlad434")
    ts4 = TestCase(1, "igor190")
    assert ts3 == ts4

    ts5= TestCase(5, "vlad9")
    ts6 = TestCase(6, "igor10")
    assert ts5 != ts6
def test_run_case():
    ts7 = TestCase(8,"Vladimir9")
    with pytest.raises(NotImplementedError):
        ts7.run_case()
    ts8 = ManualTestCase(10, "Vladimir90","Run")
    result_manual= ts8.run_case()
    assert result_manual == f"Ручное прохождение теста {ts8.name} тестировщиком {ts8.tester_name}"

    ts10 = AutomatedTestCase(12, "Igor", "Opera","x2")
    result_automated = ts10.run_case()
    assert result_automated == f"Запуск автотеста {ts10.name} в браузере {ts10.browser} на стенде {ts10.environment}"
