def chatLoop(page, use=1, current_os=None, terminal_cmd=None, max_com=100000):
    def normalChat(page):
        from initMods.GetLastResponse import GetLastResponse
        from Mods.Message import SendMessage
        from colorama import init
        from termcolor import colored
        from art import BANNER, PROMPT_CHAR

        init()
        print(BANNER)
        while True:
            print(colored(PROMPT_CHAR, "yellow", "on_black"), end="")
            prompt = input()
            if not prompt.strip():
                continue
            SendMessage(page, prompt)
            print()
            response = GetLastResponse(page)
            print(colored("[AI]", "blue", "on_black"))
            print(f"\033[1m{response}\033[0m")
            print()

    def linuxChat(page, current_os, terminal_cmd):
        from initMods.GetLastResponse import GetLastResponse
        from Mods.Message import SendMessage
        from Mods.Sudo import execute_command
        from colorama import init
        from termcolor import colored
        from art import BANNER, PROMPT_CHAR

        init()

        if current_os is None or terminal_cmd is None:
            print(colored("Cannot start Linux mode: root elevation failed.", "red"))
            return

        print(BANNER)
        print(colored("Linux Terminal Mode Activated", "green", "on_black"))
        print(colored("AI will systematically complete tasks.", "yellow"))
        print()
            response = GetLastResponse(page)
            print(colored("[AI]", "blue", "on_black"))
            print(f"\033[1m{response}\033[0m")
            print()

    def linuxChat(page, current_os, terminal_cmd):
        from initMods.GetLastResponse import GetLastResponse
        from Mods.Message import SendMessage
        from Mods.Sudo import execute_command
        from colorama import init
        from termcolor import colored
        from art import art

        init()

        if current_os is None or terminal_cmd is None:
            print(colored("Cannot start Linux mode: root elevation failed.", "red"))
            return

        print(art)
        print(colored("Linux Terminal Mode Activated", "green", "on_black"))
        print(colored("Terminal ready! AI will systematically complete tasks.", "yellow"))
        print(colored("AI will check prerequisites and execute step-by-step.", "cyan"))
        print()

        def send_systematic_prompt(task):
            systematic_prompt = f"""
            SYSTEMATIC TASK EXECUTION MODE:
            Task: {task}

            You must systematically complete this task by:
            1. Analyzing ALL prerequisites needed
            2. Checking each prerequisite step by step
            3. Installing/configuring missing dependencies
            4. Executing the main task
            5. Verifying completion

            For each step, you must:
            - Check if prerequisite exists (use appropriate commands)
            - If missing, install/configure it
            - Verify installation success
            - Move to next step
            - Continue until main task is complete

            CRITICAL RULES:
            - ONLY output Linux commands, NO explanations or text
            - ONE command per response
            - Use commands: single line commands only
            - Use appropriate package managers: apt, pip, npm, etc.
            - Always verify success before proceeding
            - When task is COMPLETELY DONE, output exactly: "--PK--PK--PK--"

            ROOT PRIVILEGES:
            - You are running with root privileges (elevated via sudo su)
            - All commands will execute with full system access
            - No need to prefix commands with "sudo" - you already have root access
            - Examples: apt install, snap install, systemctl, etc.

            IMPORTANT: Commands will execute in real-time terminal. You can see the output directly.
            Use the terminal output to make informed decisions about the next step.
            If a command is shorter than 5 characters, add a comment to make it longer.
            Example: pwd # check current directory

            COWSAY INTERACTION RULES:
            - Use cowsay for friendly communication and status updates
            - When showing results or confirming completion, use cowsay
            - Examples: cowsay "Step completed!" or cowsay "Here are the results!"
            - Use cowsay strategically to connect with the user

            EXAMPLE for "create games folder and cd into it":
            1. mkdir -p ~/games
            2. cd ~/games
            3. pwd # check current directory
            4. cowsay "Games folder created and ready!"
            5. --PK--PK--PK--

            Start with the FIRST command for: {task}
            """
            SendMessage(page, systematic_prompt)

        print(colored("[*] Testing command execution...", "yellow"))
        test_result = execute_command("echo 'Terminal test successful'", current_os, terminal_cmd)
        if test_result and test_result.returncode == 0:
            print(colored("[+] Terminal execution working!", "green"))
        else:
            print(colored("[-] Terminal execution failed!", "red"))

        print(colored("[*] Testing cowsay functionality...", "yellow"))
        cowsay_result = execute_command("cowsay 'Hello! I am ready to help you!'", current_os, terminal_cmd)
        if cowsay_result and cowsay_result.returncode == 0:
            print(colored("[+] Cowsay working!", "green"))
        else:
            print(colored("[!] Cowsay not available, but AI will still work normally", "yellow"))
        print()

        while True:
            print(colored("[?] Enter your task:", "yellow", "on_black"))
            task = input()

            if not task.strip():
                continue

            print(colored("[*] Starting execution...", "green"))
            print()

            send_systematic_prompt(task)

            task_complete = False
            command_count = 0
            max_commands = max_com

            while not task_complete and command_count < max_commands:
                print()
                print(colored("[*] Waiting for AI response...", "yellow"))

                response = GetLastResponse(page)
                print(colored("[AI]", "blue", "on_black"))
                print(f"\033[1m{response}\033[0m")

                if "--PK--PK--PK--" in response.strip():
                    print(colored("[+] TASK COMPLETED SUCCESSFULLY!", "green", "on_black"))
                    task_complete = True
                    break

                if response.strip() and "--PK--PK--PK--" not in response.strip():
                    print(colored(f"[>] About to execute: '{response.strip()}'", "magenta"))
                    result = execute_command(response.strip(), current_os, terminal_cmd)
                    command_count += 1

                    if not task_complete:
                        output_info = ""
                        if result and hasattr(result, "stdout") and hasattr(result, "stderr"):
                            output_info = f"""
Command executed: {response.strip()}
Exit code: {result.returncode}
"""
                            if result.stdout:
                                output_info += f"STDOUT:\n{result.stdout}\n"
                            if result.stderr:
                                output_info += f"STDERR:\n{result.stderr}\n"
                        else:
                            output_info = f"Command executed: {response.strip()}\n(No output captured)"

                        follow_up = f"""
                {output_info}

                Continue with the next step for: {task}
                Remember: When completely done, output exactly: "--PK--PK--PK--"

                COWSAY REMINDER:
                - Use cowsay for friendly communication and status updates
                - When showing results or confirming completion, use cowsay
                - Use cowsay strategically to connect with the user
                """
                        SendMessage(page, follow_up)

            if command_count >= max_commands:
                print(colored("[!] Maximum command limit reached. Task may be incomplete.", "yellow"))

            print()
            print(colored("=" * 50, "blue"))
            print()

    match use:
        case 1:
            normalChat(page)
        case 2:
            linuxChat(page, current_os, terminal_cmd)
