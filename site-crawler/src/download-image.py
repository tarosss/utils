import requests
import random
import time

base_url = ""
max_page = 56
for i in range(1, max_page + 1):
    url = base_url.format(i)

    for attempt in range(3):
        try:
            response = requests.get(
                url,
                timeout=30
            )

            if response.status_code == 200:
                with open(f"downloads/{i}.webp", "wb") as f:
                    f.write(response.content)

                print(f"Downloaded: {i}.webp")
                break

            print(
                f"Failed: {i}.webp "
                f"status={response.status_code} "
                f"attempt={attempt + 1}/3"
            )

        except requests.exceptions.RequestException as e:
            print(
                f"Error: {i}.webp "
                f"attempt={attempt + 1}/3: {e}"
            )

        if attempt < 2:
            wait_time = random.uniform(5, 20)
            print(f"Retrying after {wait_time:.1f} seconds...")
            time.sleep(wait_time)

    # 次の画像まで待機
    if i < 69:
        wait_time = random.uniform(5, 20)
        print(f"Waiting {wait_time:.1f} seconds...")
        time.sleep(wait_time)