def test_basic(driver):
    WAIT_SEC = 2
    driver.implicitly_wait(WAIT_SEC)

    elem = driver.find_element_by_accessibility_id('ciao')

    assert elem is not None
