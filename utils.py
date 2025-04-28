def print_result(check_name, status, message):
    """Print check results with colored output"""
    if status:
        print(f"[✓] {check_name}: \033[92m{message}\033[0m")
    else:
        print(f"[✗] {check_name}: \033[91m{message}\033[0m")

def run_command(command, sudo=False):
    """Run a system command and return output"""
    try:
        if sudo:
            command = ["sudo"] + command
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
