import os

try:
    q1 = "Has your antivirus and firewall been actively running since the last verification?"
    q2 = "Have you experienced any security issues? If yes, what? when?"
    q3 = "Name of Employee:"

    file_name = "user_responses.txt"
    response1 = input(q1)
    response2 = input(q2)
    response3 = input(q3)

    file = open(file_name, "w")
    file.write(
        f"{q1}\nResponse:{response1} \n\n{q2}\nResponse:{response2} \n\n{q3} \nResponse:{response3}")
    file.close()
except Exception as e:
    print("An exception occured: ", e)

try:
    ShowResponses = os.system('explorer "user_responses.txt"')
    ShowResponses
except Exception as e:
    print("An exception occured: ", e)

exit()
