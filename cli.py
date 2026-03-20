import click
from ai_agent.agent import AIAgent

@click.command()
@click.argument('prompt')
def main(prompt):
    agent = AIAgent()
    response = agent.respond(prompt)
    click.echo(response)

if __name__ == '__main__':
    main()
