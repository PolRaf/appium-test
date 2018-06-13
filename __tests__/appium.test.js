import wd from 'wd';

jasmine.DEFAULT_TIMEOUT_INTERVAL = 60000;
const PORT = 4723;

const config = {
    platformName: 'iOS',
    deviceName: 'iOS Emulator',
    app: './android/app/build/outputs/apk/app-debug.apk' // relative to root of project
  };
  const driver = wd.promiseChainRemote('localhost', PORT);



  beforeAll(async () => {
    await driver.init(config);
    await driver.sleep(2000); // wait for app to load
  })
  
  test('appium renders', async () => {
    expect(await driver.hasElementByAccessibilityId('ciao')).toBe(true);
    expect(await driver.hasElementByAccessibilityId('cio')).toBe(false);
  });