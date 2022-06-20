nums = []
for c in range (0, 3):
  num = int(input("Digite os numeros : "))
  if len(nums) < 0:
    print("Não pode ser vazio")
  else:
    nums.append(num)

nums.sort(reverse=True)
maior = nums[0]
menor = nums[1]
print('Maior: {}, menor {}' .format(maior, menor))
