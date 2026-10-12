# GitHub 连接操作手册

> 记录你这台电脑上 Git 环境的配置结果，以及日常怎么把代码传到 GitHub。
> 最后更新：2026-10-12

---

## 一、当前状态：代码已在 GitHub 上 ✅

| 项目 | 值 |
|---|---|
| 仓库地址 | https://github.com/Helena-lu/python-starter （公开） |
| 默认分支 | `main` |
| 已上传文件 | `main.py`、`README.md`、`.gitignore`、本手册 |
| 提交记录 | 与本地**完全一致**（哈希逐字节相同，两边不会"打架"） |
| 本地项目 | `C:\Users\Admin（无密码）\Desktop\python-starter` |

打开上面那个网址，就能看到你的代码。

---

## 二、环境配置（已完成）

| 项目 | 值 |
|---|---|
| Git 位置 | `C:\Users\Public\Git`（便携版，**不需要管理员权限**） |
| Git 命令 | `C:\Users\Public\Git\cmd\git.exe` |
| Git 版本 | 2.56.0 |
| 凭据管理器 | 已内置（`ucrt64\bin\git-credential-manager.exe`），支持浏览器一键授权 |
| 系统 PATH | 已加入 `C:\Users\Public\Git\cmd` |
| 提交署名 | `Helena-lu` / `2810232980@qq.com` |

> ⚠️ **必须完全退出 VSCode 再重新打开**，否则它读不到新加的 PATH，终端里敲 `git` 仍会报错。

---

## 三、顺带修好的一个系统故障：默认浏览器

排查过程中发现你电脑上有个真实问题：

> 系统默认浏览器被设置成了 **QQ 浏览器**（`QQBrowser.Protocol`），但 QQ 浏览器**已经被卸载**（注册表指向 `D:\Program Files\Tencent\QQBrowser\QQBrowser.exe`，文件已不存在）。
>
> 后果：**任何程序想自动打开网页都会失败**，报"找不到应用程序"。不只是 git，微信、Word 里的链接也一样点不开。

已修复：把这两条注册表项的打开命令改为指向 Edge（只改你自己的用户配置，不动系统全局）

- `HKCU\Software\Classes\QQBrowser.Protocol\shell\open\command`
- `HKCU\Software\Classes\https\shell\open\command`

原值备份在 `C:\Users\Public\browser_fix_backup.txt`。

**想彻底恢复成官方设置**：设置 → 应用 → 默认应用 → 搜索 `Edge` → 点"设为默认值"。

---

## 四、首次推送授权（下次推送时自动触发）

这次上传是用一个**访问令牌**完成的。为了安全，建议你把它**撤销**：

1. 打开 https://github.com/settings/tokens
2. 找到名字为 `workbuddy-git` 的那个令牌
3. 点 **Delete** / **Revoke**

撤销**不影响**已经上传的代码和本地环境。之后你第一次执行 `git push` 时：

- 会自动弹出 **Edge** 浏览器要求登录 GitHub
- 点一下 **Authorize** 授权即可
- 之后**永久免密**，再也不用授权

（如果那时浏览器没弹出来，用这条命令走设备码方式：`git credential-manager github login --device`）

---

## 五、日常使用（每次改完代码）

```bash
git add .                          # 1. 把改动加入暂存区
git commit -m "说明这次改了什么"     # 2. 生成一条提交记录
git push                           # 3. 推到 GitHub
```

三个命令记不住的话，记住口诀：**add → commit → push**（攒 → 存 → 传）。

想在 GitHub 上看到更新，刷新网页即可。

---

## 六、常见问题

| 情况 | 原因 | 解决 |
|---|---|---|
| `git: command not found` | 没重启 VSCode，PATH 没生效 | 完全退出 VSCode 重开 |
| 推送报 `rejected` / `fetch first` | 远程有你本地没有的提交 | 先 `git pull --rebase` 再 `git push` |
| 推送报 `Authentication failed` | 凭据失效或已撤销 | 终端执行 `git credential-manager github logout`，再 `git push` 重新授权 |
| 弹出浏览器报"找不到应用程序" | 默认浏览器关联又坏了 | 设置 → 默认应用 → 设为 Edge；或执行 `git credential-manager github login --device` |
| 提交记录里名字不对 | 署名配错了 | `git config --global user.name "Helena-lu"` |

---

## 七、关于邮箱的提醒

你用的是 QQ 邮箱 `2810232980@qq.com` 作为提交邮箱。如果希望它和你的 GitHub 账号关联（让贡献热力图统计到、同时避免公开真实邮箱），可以：

1. 打开 https://github.com/settings/emails
2. 确认 `2810232980@qq.com` 已加入；或启用 **Keep my email addresses private**，复制那个 `xxx@users.noreply.github.com` 地址
3. 告诉我，我帮你换成隐私邮箱（需要重建提交记录）
