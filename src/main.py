from rich.console import Console
from rich.prompt import Prompt

console = Console()

def main():
    console.print("[bold cyan]🔐 Welcome to SecureVault[/bold cyan]")

    while True:
        console.print("\nOptions: [green]login[/green], [yellow]create[/yellow], [red]exit[/red]")
        choice = Prompt.ask("Choose an option", choices=["login", "create", "exit"])

        if choice == "login":
            console.print("[green]Login feature coming soon...[/green]")
        elif choice == "create":
            console.print("[yellow]Vault creation coming soon...[/yellow]")
        elif choice == "exit":
            console.print("[red]Exiting...[/red]")
            break

if __name__ == "__main__":
    main()

