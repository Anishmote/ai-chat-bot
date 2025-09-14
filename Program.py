import pyautogui
import time
import pyperclip
from openai import OpenAI

while True:
    client = OpenAI(
        api_key="<ENTER YOUR API KEY HERE>")


    # thoda delay so system ko time mile
    time.sleep(6)

    # Step 1: Icon pe click (x=599, y=300)
    pyautogui.click(468,175)
    time.sleep(1)

    # Step 2: Mouse drag for selecting text
    pyautogui.moveTo(468,175)       # starting point
    pyautogui.dragTo(1262, 992, 1, button='left')  # drag leftwards, adjust coords

    time.sleep(1)

    # Step 3: Copy to clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click()

    # Step 4: Get clipboard data into variable
    chat_history = pyperclip.paste()
    print("Copied Text:", chat_history)


    response = client.responses.create(
        model="gpt-4o-mini",
    input =[
                {"role": "system", "content": "You are a person named anish who speaks hindi as well as english also marathi. You are from India and you are a coder. You analyze chat history and reply people according to situation. Output should be the next chat response (text message only)"},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
                {"role": "system", "content": "Do not add '-' like this"},
                {"role": "system", "content": "Do not reply myself iam 𝐔𝐧𝐬𝐭𝐨𝐩𝐩𝐚𝐛𝐥𝐞𝟏𝟎𝟏"},
                {"role": "user", "content": chat_history}
            ],




        
        store=True,
    )
    response = (response.output_text)


    # ---- Coordinates (replace *** with actual values) ----
    x, y = 1125, 989   # 👈 click karne ka location

    # ---- Text jo paste karna hai ----

    # Copy text to clipboard
    pyperclip.copy(response)

    # Small delay before actions
    time.sleep(2)

    # Step 1: Click on given coordinates
    pyautogui.click(x, y)

    # Step 2: Paste clipboard text (Ctrl+V)
    pyautogui.hotkey("ctrl", "v")

    # Step 3: Press Enter
    pyautogui.hotkey("enter")
