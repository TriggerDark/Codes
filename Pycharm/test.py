import re
import xlwt

"""获取文件信息"""
def read_file_csv(file_name):
    with open(file_name, "r",encoding='UTF-8')as f:
        cont = f.readlines()
        return [cont[i].strip("\n") for i in range(len(cont))]


"""用于用户名判断 自己去调整 ---> 找正则表达式"""
def deal_Name(name):
    return bool(re.match(r'^[\w\u4E00-\u9FA5\uF900-\uFA2D-； ]{3,10}$', name))
    #return bool(re.match(r'^[\w\u4E00-\u9FA5\uF900-\uFA2D-； ]+$', name))


"""用于分支判断 自己去调整 ---> 找正则表达式"""
def deal_branch(name):
    if "changed" in name:
        return True
    return False


"""获取索引"""
def deal_index(cont, deal_function):
    index = []
    for i in range(len(cont)):
        if deal_function(cont[i]):
            index.append(i)
    return index


"""按用户名进行分组"""
def deal_info_nameIndex(cont, name_index):
    deal_author_info = []
    name_index.append(len(info))
    for i in range(len(name_index) - 1):
        deal_info = []
        [deal_info.append(cont[j]) for j in range(name_index[i], name_index[i+1])]
        deal_author_info.append(deal_info)
    return deal_author_info


def deal_to_dict(deal_author_info, deal_branch):
    deal_dict_list = []
    for i in range(len(deal_author_info)):
        deal_single_dict = {}
        index = deal_index(deal_author_info[i], deal_branch)
        index.insert(0, 0)
        if len(deal_author_info[i]) == 1:
            deal_single_dict["作者"] = deal_author_info[i][0]
            deal_dict_list.append(deal_single_dict)
        elif len(deal_author_info[i]) > 1:
            for j in range(len(index) - 1):
                content_all = ""
                for k in range(index[j] + 2, index[j+1]):
                    content_all += deal_author_info[i][k] + "\n"
                deal_single_dict = deal_single_dict.copy()
                deal_single_dict["作者"] = deal_author_info[i][0]
                deal_single_dict["分支"] = deal_author_info[i][index[j]+1]
                deal_single_dict["内容"] = content_all
                deal_single_dict["总计"] = deal_author_info[i][index[j+1]]
                deal_dict_list.append(deal_single_dict)
    return deal_dict_list


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
    workbook.save('Code_Statistics2.xls')



if __name__ == "__main__":
    info = read_file_csv("fontt-onepy.csv")
    #info = read_file_csv("gittagt1.csv")
    name_index = deal_index(info, deal_Name)
    deal_author_info = deal_info_nameIndex(info, name_index)
    deal_dict_list = deal_to_dict(deal_author_info, deal_branch)
    dict_to_excel(deal_dict_list)