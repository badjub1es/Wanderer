from flask.cli import AppGroup
from .users import seed_users, undo_users
from .room_types import seed_room_types, undo_seed_room_types
from .listings import seed_listings, undo_seed_listings
from .images import seed_images, undo_seed_images
from .reservations import seed_reservations, undo_reservations
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_room_types()
    seed_listings()
    seed_images()
    seed_reservations()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_seed_room_types()
    undo_seed_images()
    undo_reservations()
    undo_seed_listings()
    # Add other undo functions here
