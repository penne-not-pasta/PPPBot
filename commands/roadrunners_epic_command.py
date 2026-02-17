import discord

async def roadrunner(interaction: discord.Interaction):
	await interaction.response.send_message(":road:")


module = {
	"type": "command",
	"name": "roadrunner",
	"description": "sends a little roadrunner",
	"callback": roadrunner
}
