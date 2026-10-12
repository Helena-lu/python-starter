# GitHub 连接操作手册

> 这份文档记录你电脑上 Git 环境的配置结果，以及日常怎么把代码传到 GitHub。

## 一、环境现状（已配置完成）

| 项目 | 值 |
|---|---|
| Git 位置 | `C:\Users\Public\Git`（便携版，无需管理员权限） |
| Git 命令 | `C:\Users\Public\Git\cmd\git.exe` |
| Git 版本 | 2.56.0 |
| 凭据管理器 | 已内置（`ucrt64\bin\git-credential-manager.exe`），支持浏览器授权免密 |
| 系统 PATH | 已加入 `C:\Users\Public\Git\cmd` |
| 提交署名 | Helena-lu / 2810232980@qq.com |
| 项目位置 | `C:\Users\Admin（无密码）\Desktop\python-starter` |
| 远程仓库 | https://github.com/Helena-lu/python-starter.git |

> ⚠️ **必须完全退出 VSCode 再重新打开**，否则它读不到新加的 PATH，终端里敲 `git` 仍会报错。

## 二、只剩两步

### 第 1 步：在 GitHub 网页上建一个空仓库

1. 浏览器打开 https://github.com/new
2. **Repository name** 填：`python-starter`
3. 选 **Public**（公开）或 Private（私有）都可以
4. ⚠️ **不要勾选** "Add a README file"、不要选 .gitignore 和 license
   （勾了会和你本地已有的提交冲突，推送会报错）
5. 点绿色按钮 **Create repository**

### 第 2 步：推送代码

在 VSCode 里打开文件夹 `python-starter`，打开终端（`` Ctrl+` ``），粘贴：

```bash
git push -u origin main
```

回车后会**自动弹出浏览器**要求登录 GitHub → 点 **Authorize** 授权。

看到类似这段就成功了：

```
To https://github.com/Helena-lu/python-starter.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

然后刷新 GitHub 网页，代码就上去了。

## 三、日常使用（每次改完代码）

```bash
git add .                          # 1. 把改动加入暂存区
git commit -m "说明这次改了什么"     # 2. 生成一条提交记录
git push                           # 3. 推到 GitHub（首次之后不再需要授权）
```

三个命令记不住的话，记住这个口诀：**add → commit → push**（攒 → 存 → 传）。

## 四、常见问题

| 情况 | 原因 | 解决 |
|---|---|---|
| `git: command not found` | 没重启 VSCode，PATH 没生效 | 完全退出 VSCode 重开 |
| 推送报 `rejected` / `fetch first` | 远程仓库不是空的 | 删掉 GitHub 上那个仓库重建，别勾 README |
| 推送报 `Authentication failed` | 凭据失效 | 终端执行 `git credential-manager github logout` 后重推 |
| 提交记录里名字不对 | 署名配错了 | `git config --global user.name "Helena-lu"` |

## 五、关于邮箱的提醒

你用的是 QQ 邮箱 `2810232980@qq.com` 作为提交邮箱。如果希望它和你的 GitHub 账号关联（让贡献热力图统计到、避免暴露真实邮箱），可以：

1. 打开 https://github.com/settings/emails
2. 确认 `2810232980@qq.com` 已加入，或启用 **Keep my email addresses private** 并复制那个 `xxx@users.noreply.github.com` 地址
3. 告诉我，我帮你换成隐私邮箱
