import xml.etree.ElementTree as et

# check temp.xml
def tempParse ():
    # tree = et.ElementTree(file="./data/temp.xml")
    tree = et.parse("./data/temp.xml")
    root = tree.getroot()
    print("root : ", root)
    print("root tag : ", root.tag)

#print tag and text
    for reef in root:
        for grandReef in reef:
            print(grandReef.tag, "/",  grandReef.text)
# tempParse()
print()

def temp2Parse():
    tree = et.parse("./data/temp2.xml")
    root = tree.getroot()
    print("root : ", root)
    print("root tag : ", root.tag)

#print tag and text
    for reef in root:
        for grandReef in reef:
            print(grandReef.tag, "/",  grandReef.text)

# temp2Parse()

def fruitParse():
    tree = et.parse("./data/sample.xml")
    root = tree.getroot()
    item = []
    # print(root)
    for items in root:
        item.append(items.tag)

    item = set(item)
    print(item)

    totalPrice = 0

    for type in item:

        # for items in root.findall("fruit"):
        for items in root.findall(type):
            name = items.find("name").text
            price = int(items.find("price").text)
            count = int(items.find("count").text)

            total = price * count
            print(f"{name} 단가 : {price}   수량 : {count}    금액 : {total}  ")

            totalPrice += total
            # print(type(items))
    print()
    print(f"합계 금액 : {totalPrice}")
fruitParse()
