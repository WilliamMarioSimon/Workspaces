from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule


def book_library_seat():
    # 初始化 WebDriver
    driver = webdriver.Chrome()  # 确保 chromedriver 在系统 PATH 中
    wait = WebDriverWait(driver, 10)  # 显式等待

    try:
        # 1. 访问预约网站
        driver.get("http://icspace.lib.zjhu.edu.cn/")

        # 2. 登录账户
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("your_username")  # 替换账号
        driver.find_element(By.ID, "password").send_keys("your_password")  # 替换密码
        driver.find_element(By.ID, "login_button").click()  # 登录按钮
        time.sleep(2)

        # 3. 进入预约界面
        driver.find_element(By.LINK_TEXT, "进入预约").click()  # 视网站具体入口调整
        time.sleep(2)

        # 4. 选择座位
        # 选择楼层或区域（示例是默认选择第1个区域）
        driver.find_element(By.XPATH, "//div[@class='room'][1]").click()
        time.sleep(1)

        # 选择时间段和具体座位
        driver.find_element(By.XPATH, "//button[contains(text(), '10:00-12:00')]").click()  # 修改为所需时间段
        driver.find_element(By.XPATH, "//span[contains(text(), '座位001')]").click()  # 替换为偏好座位
        time.sleep(1)

        # 5. 提交预约
        driver.find_element(By.ID, "submit_button").click()
        print("预约成功！")

    except Exception as e:
        print(f"发生错误：{e}")

    finally:
        # 关闭浏览器
        driver.quit()


# 定时运行任务
if __name__ == "__main__":
    # 每天定时运行任务（比如早上7点30分）
    schedule.every().day.at("07:30").do(book_library_seat)

    while True:
        schedule.run_pending()
        time.sleep(1)
