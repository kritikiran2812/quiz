import mysql.connector as my
import random

con = my.connect(host="localhost", user="root", password="", database="quiz")
cur = con.cursor()

"""check wether connectiom is established or not"""
# print(con)

username = ""
logged_in = False


def main():
    print("= " * 10 + "QUIZ" + " " + "= " * 10)
    print(
        """
            1. Register
            2. Login
            3. Attempt Quiz
            4. Exit
        """
    )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        attemptQuiz()
    elif choice == 5:
        leave()
    else:
        print("please enter correct choice")
        main()


def register():
    name = input("enter your name\n")
    enr = input("enter your enrollment number\n")
    clg = input("enter your college name\n")
    psw = input("enter your password\n")
    cont = input("enter your contact number\n")
    data = (name, enr, clg, psw, cont)
    sql = "insert into register (name,enrollment, college, password, contact) values(%s,%s,%s,%s,%s)"

    cur.execute(sql, data)
    con.commit()
    print("You have been registered successfully")


def login():
    global username
    global logged_in
    uname = input("enter username\n")
    cur.execute("select * from register where name = %s", (uname,))
    data = cur.fetchone()
    # print(data)
    if data is not None:
        pwd = input("enter password: ")
        if data[3] == pwd:
            print(f"welcome {data[0]}")
            username = uname
            logged_in = True
        else:
            print("wrong password")
    else:
        print("wrong username or you are not a registered user!!")
        ch = input("Do you want to register? enter y/n:")
        if ch == "y" or ch == "Y":
            register()
        else:
            main()
    print("Are you ready to attend the QUIZ !!\n")
    ch = input("enter your choice Y/N: ").lower()
    if ch == "y":
        attemptQuiz(username)
    elif ch == "n":
        leave()
    else:
        print("enter a valid choice")


def attemptQuiz(uname):
    ch = int(input("choose an option \n 1. Python\n 2. Maths\n"))
    if ch == 1:
        sql = "select * from questions where category = 'Python'"
        cur.execute(sql)
        ques = cur.fetchall()
        # print(ques)
        qu = []
        for i in ques:
            qu.append(i)
        # print(qu)
        qs = random.sample(qu, 2)
        # print(qs)
        n = 1
        correct = 0
        for i in qs:
            print(f"Hello {uname} you are attempting quiz of {i[0]}")
            print(f"Q.{n}.{i[1]}\n 1. {i[2]}\n 2. {i[3]}\n 3. {i[4]}\n 4. {i[5]}\n")
            ans = int(input("Your Answer 1/2/3/4: "))
            if ans == i[-1]:
                correct += 1

            n = n + 1
        print(f"\nYour score is {correct}")
    elif ch == 2:
        sql = "select * from questions where category = 'Maths'"
        cur.execute(sql)
        ques = cur.fetchall()
        # print(ques)
        qu = []
        for i in ques:
            qu.append(i)
        # print(qu)
        qs = random.sample(qu, 4)
        # print(qs)
        n = 1
        correct = 0
        for i in qs:
            print(f"Q.{n}. {i[1]}\n A. {i[2]}\n B. {i[3]}\n C. {i[4]}\n D. {i[5]}\n")
            ans = input("Your Answer A/B/C/D: ").upper()
            if ans == i[-2]:
                correct += 1

            n = n + 1
        print(f"Your score is {correct}")


def leave():
    print("\nThanks foer visiting!!!")
    exit()


if __name__ == "__main__":
    main()
