import socket

LOCALHOST = "127.0.0.1"
PORT = 5040

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

clientConnection, clientAddress = server.accept()

msg = ''
array = []

while True:
    data = clientConnection.recv(1024)
    message = data.decode()

    if message == 'Exit':
        print("Соединение прервано")
        break

    print("Результат")
    result = 0
    operation_list = message.split()
    first_num = operation_list[0]
    num1 = int(first_num)

    if len(operation_list) == 3:

        operation = operation_list[1]
        second_num = operation_list[2]
        number2 = int(second_num)

        if operation == "+":
            result = num1 + number2
        elif operation == "-":
            result = num1 - number2
        elif operation == "/":
            result = num1 / number2
        elif operation == "*":
            result = num1 * number2
        array.append(result)
        output = str(result)

    elif len(operation_list) == 2:
        operation = operation_list[1]
        if operation == "+":
            result = array[len(array) - 1] + num1
        elif operation == "-":
            result = array[len(array) - 1] - num1
        elif operation == "/":
            result = array[len(array) - 1] / num1
        elif operation == "*":
            result = array[len(array) - 1] * num1
        array.append(result)
        output = str(result)

    elif len(operation_list) == 1:
        if operation_list[0] == 'history':
            result = ''
            for i in array:
                result = result + ' ' + str(i)
            output = result
            clientConnection.send(output.encode())
        else:
            output = 'Что ты такое отправил...'

    clientConnection.send(output.encode())
clientConnection.close()
