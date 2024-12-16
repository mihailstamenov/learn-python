# fruits = ['grape','apple', 'banana', 'grape']
# alt =  list(set(fruits))
# fruits_set = set(fruits)
# fruits = list(fruits_set)
# print(fruits)

str = "A Cloud Connector is a software or hardware solution that enables the integration of on-premises systems and applications with cloud-based services. It acts as a bridge to facilitate seamless data exchange and communication between local systems and cloud environments, allowing organizations to leverage the benefits of both."

vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
count = 0
for char in str:
    if char in vowels:
        count += 1

print(count)