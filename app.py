# app.py - Created by Saloni Prajapati
def greet(name):
    return f"Hello, {name}! Welcome to INFO 52170."

def info(name,school):
    return f"{name} is enrolled in IT Project Management course at {school} college."

if __name__ == "__main__":
    print(greet("Saloni"))
    print(info("Saloni","Sheridan"))