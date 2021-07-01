# https://www.urionlinejudge.com.br/judge/en/problems/view/1048

salary = float(input())
percent = 0

if(salary > 0 and salary <= 400):
    newSalary = (salary + (salary * 0.15))
    percent += 15
elif(salary > 400 and salary <= 800):
    newSalary = (salary + (salary * 0.12))
    percent += 12
elif(salary > 800 and salary <= 1200):
    newSalary = (salary + (salary * 0.1))
    percent += 10
elif(salary > 1200 and salary <= 2000):
    newSalary = (salary + (salary * 0.07))
    percent += 7
else:
    newSalary = (salary + (salary * 0.04))
    percent += 4

increase = newSalary - salary
print(f'Novo salario: {newSalary:.2f}')
print(f'Reajuste ganho: {increase:.2f}')
print(f'Em percentual: {percent} %')

