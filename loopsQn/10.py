# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time
wait_time = 1
max_tries = 5
attempt = 0

if(attempt >= max_tries):
    print("Sorry you have no more attempts left")

while(attempt<max_tries):
    print("ATTEMPT ->", attempt, "--wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1
