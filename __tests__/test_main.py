def test_basic(driver):
    WAIT_SEC = 20
    driver.implicitly_wait(WAIT_SEC)

    btn = driver.find_element_by_accessibility_id('button')
    counter = driver.find_element_by_accessibility_id('counter')
    assert counter.text == 'not_clicked'

    btn.click()

    assert counter.text == 'clicked'


    assert btn is not None
    assert counter is not None
