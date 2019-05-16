import xlwt
import re
import sys

"""读取文件"""
# def read_file(fileName):
#     b = []
#     with open(fileName, 'r') as f:
#         a = f.readlines()
#     for i in range(len(a)):
#         b.append(a[i].strip('\n'))
#     return b

def read_file_csv(file_name):
    with open(file_name, "r",encoding='UTF-8')as f:
        cont = f.readlines()
        return [cont[i].strip("\n") for i in range(len(cont))]


"""正则表达：字符串中是否有数字"""
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


def con_flag(s):
    flag = True
    for item in ["(", ")", "-", "/", ":", "."]:
        if item in s:
            flag = False
            break
    return flag


"""处理数据 列表->字典->列表"""
def deal_data(cont_list=[]):
    return_list = []  # 用于返回数据
    index = 0  # cont_list 索引
    n = len(cont_list)
    while True:
        if index < n:
            dir_single = {}
            if con_flag(cont_list[index]):
                i = index
                index += 1
                if index < n:
                    while True:
                        branch_split = cont_list[index].split(" ")
                        if hasNumbers(branch_split[0]):
                            j = index
                            index += 1
                            str_all = ""
                            while True:
                                if "." in cont_list[index]:
                                    str_all += cont_list[index] + "\n"
                                    index += 1
                                else:
                                    break
                            dir_single = dir_single.copy()
                            dir_single["作者"] = cont_list[i]
                            dir_single["分支"] = cont_list[j]
                            dir_single["内容"] = str_all.strip("\n")
                            dir_single["总计"] = cont_list[index]
                            return_list += [dir_single]
                            index += 1
                        else:
                            if dir_single.get("分支", "") != "":
                                del dir_single
                                break
                            else:
                                dir_single["作者"] = cont_list[i]
                                return_list += [dir_single]
                                break
                else:
                    dir_single["作者"] = cont_list[i]
                    return_list += [dir_single]
                    index += 1
                    break
            else:
                index += 1
        else:
            break
    return return_list


def dict_to_excel(dataList):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('details')

    worksheet.write(0, 0, "开始时间")
    worksheet.write(0, 1, "结束时间")
    worksheet.write(0, 2, "作者")
    worksheet.write(0, 3, "分支")
    worksheet.write(0, 4, "内容")
    worksheet.write(0, 5, "总计")
    worksheet.write(0, 6, "修改文件数")
    worksheet.write(0, 7, "增加行数")
    worksheet.write(0, 8, "删除行数")
    开始时间 = "2019-05-01"
    结束时间 = "2019-05-30"
    val = 1
    for list_item in dataList:
        worksheet.write(val, 0, 开始时间)
        worksheet.write(val, 1, 结束时间)
        for key, value in list_item.items():
            if key == "作者":
                worksheet.write(val, 2, value)
            elif key == "分支":
                worksheet.write(val, 3, value)
            elif key == "内容":
                worksheet.write(val, 4, value)
            elif key == "总计":
                worksheet.write(val, 5, value)
                str_split = value.strip(" ").split(", ")
                for i in str_split:
                    str_split_single = i.strip(" ").split(" ")
                    if "changed" in i:
                        worksheet.write(val, 6, str_split_single[0])
                    elif "insertion" in i:
                        worksheet.write(val, 7, str_split_single[0])
                    else:
                        worksheet.write(val, 8, str_split_single[0])
        val += 1
    workbook.save('Code_Statistics.xls')
    # workbook.save(sys.argv[3])

"""main"""
# if __name__ == '__main__':
#     b = read_file(sys.argv[4])
#     dataList = dealData(b)
#     dict_to_excel(dataList)
if __name__ == "__main__":
    # file_name = "preliminary.csv"
    file_name = "fontt-onepy.csv"
    result = deal_data(read_file_csv(file_name))
    dict_to_excel(result)