import subprocess
import getpass
import webbrowser, os

def backup_mysql_db():
    host = input("Digite o host do banco de dados (ex: localhost): \n")
    user = input("Digite o usuário do banco de dados: \n")
    password = getpass.getpass("Digite a senha do banco de dados: \n")
    database = input("Digite o nome do banco de dados: \n")
    dir_mysql = [
    "C:/Program Files/MySQL/MySQL Server 5.6/bin/",
    "C:/Program Files/MySQL/MySQL Server 5.7/bin/"
]
    dir_bin = None
    
    for dir_path in dir_mysql:
        if os.path.exists(dir_path): 
            dir_bin = dir_path  
            break 
    
    if dir_bin:
        print(f"Caminho do mysqldump encontrado: {dir_bin}")
    else:
        print("Caminho não encontrado! Por favor, verifique a instalação no disco local C.") 
    
    
    dump_option = input("Você quer fazer o dump de todo o schema (S) ou apenas de uma tabela (T)? ").strip().upper()
    if dump_option == 'S':
        backup_file = input("Digite o caminho completo do arquivo de backup (deixe em branco para usar o padrão): ").strip()
        if not backup_file:
            default_backup_dir = "C:/dump" 
            if not os.path.exists(default_backup_dir):
                os.makedirs(default_backup_dir)
            backup_file = os.path.join(default_backup_dir, f"{database}_full_backup.sql")    
        dump_exec = f"cd {dir_bin} && mysqldump -h {host} -u {user} -p{password} {database} > {backup_file}"
    elif dump_option == 'T':
        table_name = input("Digite o nome da tabela: ")
        backup_file = input("Digite o caminho completo do arquivo de backup (deixe em branco para usar o padrão): ").strip()
        if not backup_file:
            default_backup_dir = "C:/dump"
            if not os.path.exists(default_backup_dir):
                os.makedirs(default_backup_dir)
            backup_file = os.path.join(default_backup_dir, f"{database}_{table_name}_backup.sql")
        dump_exec = f"cd {dir_bin} && mysqldump -h {host} -u {user} -p{password} {database} {table_name} > {backup_file}"
    else:
        print("Opção inválida. Use 'S' para schema ou 'T' para tabela.")
        return
    
    
    
    try:
        subprocess.run(dump_exec, shell=True, check=True)
        print(f"Backup realizado com sucesso no arquivo {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao realizar o backup: {e}")

if __name__ == "__main__":
    backup_mysql_db()
