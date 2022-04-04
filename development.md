# 网站修改，保存和发布说明

2022-4-1

## 安装Jekyll

### Mac安装（使用Homebrew）

安装Ruby
```
brew install chruby ruby-install
ruby-install ruby
```

配置环境变量默认使用chruby
```
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
echo "chruby ruby-3.1.1" >> ~/.zshrc
```

检查ruby的可用性
```
ruby -v
```

安装Jekyll
```
gem install jekyll
```

### Windows安装
有点复杂，参见：https://jekyllcn.com/docs/installation/

## 使用自己的Github账号编辑该仓库

### 配置自己电脑的git环境
[初次运行git前的配置](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%88%9D%E6%AC%A1%E8%BF%90%E8%A1%8C-Git-%E5%89%8D%E7%9A%84%E9%85%8D%E7%BD%AE)

### 将自己电脑的密钥添加到用户
在用户Settings->SSH and GPG keys->new SSH key
添加并确认

### 将Github账号添加至仓库贡献者权限
在该页面：
https://github.com/kexinlilab/kexinlilab.github.io

Setings->Access->Collaborators邀请用户（个人Github用户）

### 克隆这个仓库到本地

```sh
https://github.com/kexinlilab/kexinlilab.github.io.git
```

## 修改网页内容

### 图片
图片都放在images文件夹下，需要图片先放在其子文件夹内

### 其他内容
在_data文件夹下进行修改：
- 新闻：news.yml
- 活动照片页面：pictures_leiden.yml (照片文件夹是images/picpic)
- 发表文章列表：publist.yml
- 成员（员工）：staff.yml
- 成员（硕士研究生）：students.yml
- 成员（博士研究生）：team_members.yml
- 成员（访问学生）：visitings.yml
成员图片文件夹：pictures/teampic

### 页面内容与排版
修改_pages文件夹下的内容， 使用markdown和html语言均可。
注意：页面与_data之间的联系使用特殊的语法
例如：_pages/team.md中对所有各条信息的链接语句为
```
line15: {% for member in site.data.staff %}
```

## 修改完成后预览
在本地仓库文件夹下运行：
```sh
jeklly server
```

使用显示的Server address在本地浏览器打开网页进行预览

## 上传到Github

```sh
git add --all
git commit -m "Update Website"
git push origin master
```
