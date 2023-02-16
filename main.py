import requests, os, time, random, threading
live = 0
Accdie = 0
INFO = '\033[1;31m[\033[1;37mINFO\033[1;31m]\033[1;37m :'


class CheckLive:
    def __init__(self, user: str) -> None:
        global listAcc
        self.user = user
        
    def checkLive(self):
        global live, Accdie
        s = requests.Session()
        for x  in range(15):
            die = False
            try:
                check = s.get(url = f'https://now.tiktok.com/@{self.user}').text
                if '"nickname":"' in check:
                    unqueName = check.split('"nickname":"')[1].split('"')[0]
                    live+=1
                    if  "musically-maliva-obj" in check:
                        return "NO_AVT", unqueName
                    else:
                        return "AVT_OK", unqueName
                else:
                    die = True
            except:pass
        if die == True:Accdie+=1; return "DIE", None
        else: return "ERROR", None
        
def fashBanner():
    os.system('cls')
    logo = '''
{}████████╗██╗░░░░░░██████╗███████╗
{}╚══██╔══╝██║░░░░░██╔════╝██╔════╝
{}░░░██║░░░██║░░░░░╚█████╗░█████╗░░
{}░░░██║░░░██║░░░░░░╚═══██╗██╔══╝░░
{}░░░██║░░░███████╗██████╔╝██║░░░░░
{}░░░╚═╝░░░╚══════╝╚═════╝░╚═╝░░░░░
    '''.format(random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']), random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']), random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']), random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']), random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']), random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']))
    print(logo)
    print('\033[1;37m'+'- '*40)
    print(f'{INFO} \033[1;32mZalo: \033[1;33m0398206564 ')
    print(f'{INFO} \033[1;32mFacebook: \033[1;33mFacebook.com/taile.official.2006')
    print(f'{INFO} \033[1;32mBạn Đang Sử Dụng Tool: \033[1;33mCheck INFO TikTok')
    print('\033[1;37m'+'- '*40)
    
def checkLiveAccount(acc: str):
    try:
        if "\n" in acc: acc = acc.replace('\n', '')
        user = acc.split("|")[0]
        tik = CheckLive(user)
        check = tik.checkLive()
        er = ["ERROR", "DIE"]
        av = ['AVT_OK', 'NO_AVT']
        if check[0] in er: print(f'{INFO} \033[1;37mUser:\033[1;33m {user}\033[1;37m => \033[1;31m[\033[1;31m{er[er.index(check[0])]}\033[1;31m]')
        elif check[0] in av: print(f'{INFO} \033[1;37mUser: \033[1;33m{user}\033[1;37m => Name:\033[1;33m {check[1]} \033[1;37m[\033[1;32mLIVE\033[1;37m] => \033[1;33m{av[av.index(check[0])]}')
        open(check[0]+'.txt', 'a+').write(acc+'\n')
    except Exception as e:print(e)
    
def main():
    for x in range(100):
        try:
            acc = next(iterAcc)
            threading.Thread(target=checkLiveAccount, args=(acc,)).start(); break
        except Exception as e:print(e)
    
active = True
if active == True:
    fashBanner()
    while(True):
        if os.path.exists('acc.txt') == False: open('acc.txt', 'w+')
        listAcc = open('acc.txt', 'r').readlines()
        try:
            listAcc.remove('')
        except:
            pass
        if listAcc == []:
            print("File acc rỗng, thêm acc vào file acc.txt, load lại sau 5 giây...", end="\r")
            time.sleep(5)
            continue
        break
    iterAcc = iter(listAcc)
    fashBanner()
    print(f'{INFO}\033[1;32m Tổng số account TikTok: \033[1;33m{len(listAcc)}\033[1;32m tài khoản')
    print('\033[1;37m'+'- '*40)
    for x in range(len(list(listAcc))):
        if threading.active_count()>500:time.sleep(5)
        threading.Thread(target=main).start()

    def count():
        while(True):
            if threading.active_count() > 2:
                pass
            else:
                time.sleep(1.5)
                print(INFO+' \033[1;36mTotal: \033[1;33m{} \033[1;32mLIVE\033[1;37m: \033[1;33m{}\033[1;31m - \033[1;37m\033[1;31mDIE\033[1;37m: \033[1;33m{}\033[1;31m'.format(len(listAcc),live, Accdie), end='\r')
                break
    threading.Thread(target = count).start()
input()
