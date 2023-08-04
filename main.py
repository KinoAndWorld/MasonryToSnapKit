import os
import sys
import re

def searchFiles():
    # 搜索文件夹路径
    # folder_path = '/Users/kino/YY-Work/Direct-Haokan/YYULiveSDK-ios/yyulivesdk'
    folder_path = '/Users/kino/YY-Work/Direct-Haokan/YYULiveSDK-ios/yyulivesdk/SupportBusiness/Channel/Modules/SachetTeamModule'
    print(f"正在搜索{folder_path}内的文件...")
    # 要替换的字符串和替换后的字符串
    replaceMap = {
        'mas_makeConstraints': 'snp.makeConstraints',
        'mas_updateConstraints': 'snp.updateConstraints',
        'mas_remakeConstraints': 'snp.remakeConstraints',
        'mas_left': 'snp.left',
        'mas_top': 'snp.top',
        'mas_right': 'snp.right',
        'mas_bottom': 'snp.bottom',
        'mas_leading': 'snp.leading',
        'mas_trailing': 'snp.trailing',
        'mas_width': 'snp.width',
        'mas_height': 'snp.height',
        'mas_centerX': 'snp.centerX',
        'mas_centerY': 'snp.centerY',
        'mas_baseline': 'snp.baseline',
        'mas_firstBaseline': 'snp.firstBaseline',
        'mas_lastBaseline': 'snp.lastBaseline',
        'mas_leftMargin': 'snp.leftMargin',
        'mas_rightMargin': 'snp.rightMargin',
        'mas_topMargin': 'snp.topMargin',
        'mas_bottomMargin': 'snp.bottomMargin',
        'mas_leadingMargin': 'snp.leadingMargin',
        'mas_trailingMargin': 'snp.trailingMargin',
        'mas_centerXWithinMargins': 'snp.centerXWithinMargins',
        'mas_centerYWithinMargins': 'snp.centerYWithinMargins',
        'mas_safeAreaLayoutGuide': 'snp.safeAreaLayoutGuide',
        'mas_safeAreaLayoutGuideTop': 'snp.safeAreaLayoutGuideTop',
        'mas_safeAreaLayoutGuideBottom': 'snp.safeAreaLayoutGuideBottom',
        'mas_safeAreaLayoutGuideLeft': 'snp.safeAreaLayoutGuideLeft',
        'mas_safeAreaLayoutGuideRight': 'snp.safeAreaLayoutGuideRight',
        'make?': 'make',
        'maker?': 'maker',
        'mas_equalTo()': 'equalTo',
        'equalTo()': 'equalTo',
        'mas_greaterThanOrEqualTo()': 'greaterThanOrEqualTo',
        'mas_lessThanOrEqualTo()': 'lessThanOrEqualTo',
        'greaterThanOrEqualTo()': 'greaterThanOrEqualTo',
        'lessThanOrEqualTo()': 'lessThanOrEqualTo',
        'left().': 'left.',
        'top().': 'top.',
        'right().': 'right.',
        'bottom().': 'bottom.',
        'leading().': 'leading.',
        'trailing().': 'trailing.',
        'width().': 'width.',
        'height().': 'height.',
        'centerX().': 'centerX.',
        'centerY().': 'centerY.',
        'baseline().': 'baseline.',
    }

    pattern_reps = ['inset',
                   'sizeOffset',
                   'centerOffset',
                   'offset',
                   'valueOffset',
                   'multipliedBy',
                   'dividedBy']

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 判断文件后缀是否为.swift
            if file.endswith('.swift'):
                # 打开文件并读取内容
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    contentLines = f.readlines()

                new_contens = []
                for line in contentLines:
                    # 替换字符串并写入文件
                    # new_content = content.replace(old_str, new_str)
                    # 遍历替换映射表中的所有键和值，并将文本中的匹配项替换为目标字符串
                    for old_str, new_str in replaceMap.items():
                        line = line.replace(old_str, new_str)

                    # 二级修改
                    # 要匹配的正则表达式
                    for par_comp in pattern_reps:
                        pattern = r'\?\.{}\(\)'.format(par_comp)
                        # 使用正则表达式进行匹配和替换
                        replacement = "." + par_comp
                        line = re.sub(pattern, replacement, line)

                    # 如果以.equalTo结尾
                    if line.endswith('.equalTo'):
                        # 将.equalTo替换为.equalTo(snp.equalTo)
                        line = line.replace('.equalTo', '.equalToSuperview()')
                    new_contens.append(line)

                # 拼回字符串
                content = ''.join(new_contens)

                with open(file_path, 'w') as f:
                    f.write(content)

                print(f'{file} 替换完成')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    searchFiles()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
