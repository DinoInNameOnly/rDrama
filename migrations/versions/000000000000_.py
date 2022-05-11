"""empty message

Revision ID: 000000000000
Revises: 
Create Date: 2022-05-11 23:27:46.576111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '000000000000'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comments', 'oauth_apps', ['app_id'], ['id'])
    op.alter_column('commentvotes', 'vote_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('commentvotes', 'real',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('commentvotes', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('commentvotes_comments_type_index', table_name='commentvotes')
    op.drop_index('cvote_user_index', table_name='commentvotes')
    op.create_foreign_key(None, 'commentvotes', 'oauth_apps', ['app_id'], ['id'])
    op.alter_column('exiles', 'exiler_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('fki_exile_exiler_fkey', table_name='exiles')
    op.drop_index('fki_exile_sub_fkey', table_name='exiles')
    op.alter_column('flags', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('flag_user_idx', table_name='flags')
    op.alter_column('follows', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('follow_user_id_index', table_name='follows')
    op.alter_column('marseys', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('marseys', 'tags',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('marseys', 'count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.drop_index('marseys_idx', table_name='marseys')
    op.drop_index('marseys_idx2', table_name='marseys')
    op.drop_index('marseys_idx3', table_name='marseys')
    op.alter_column('modactions', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('fki_modactions_user_fkey', table_name='modactions')
    op.drop_index('modaction_action_idx', table_name='modactions')
    op.drop_index('modaction_cid_idx', table_name='modactions')
    op.drop_index('modaction_id_idx', table_name='modactions')
    op.drop_index('modaction_pid_idx', table_name='modactions')
    op.create_foreign_key(None, 'modactions', 'users', ['user_id'], ['id'])
    op.alter_column('mods', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('fki_mod_sub_fkey', table_name='mods')
    op.alter_column('notifications', 'read',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('notifications', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('notification_read_idx', table_name='notifications')
    op.drop_index('notifications_comment_idx', table_name='notifications')
    op.drop_index('notifs_user_read_idx', table_name='notifications')
    op.alter_column('oauth_apps', 'app_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('oauth_apps', 'redirect_uri',
               existing_type=sa.VARCHAR(length=4096),
               nullable=True)
    op.alter_column('oauth_apps', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('oauth_apps', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('unique_id', 'oauth_apps', type_='unique')
    op.drop_index('fki_save_relationship_submission_fkey', table_name='save_relationship')
    op.drop_index('fki_sub_blocks_sub_fkey', table_name='sub_blocks')
    op.add_column('submissions', sa.Column('bump_utc', sa.Integer(), server_default=FetchedValue(), nullable=True))
    op.alter_column('submissions', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('submissions', 'edited_utc',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('submissions', 'is_banned',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'ghost',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'views',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'deleted_utc',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'distinguish_level',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'is_pinned',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'private',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'club',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'comment_count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'over_18',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'is_bot',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'upvotes',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('1'))
    op.alter_column('submissions', 'downvotes',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'title',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('submissions', 'title_html',
               existing_type=sa.VARCHAR(length=1500),
               nullable=True)
    op.drop_index('fki_submissions_approver_fkey', table_name='submissions')
    op.drop_index('post_app_id_idx', table_name='submissions')
    op.drop_index('subimssion_binary_group_idx', table_name='submissions')
    op.drop_index('submission_isbanned_idx', table_name='submissions')
    op.drop_index('submission_isdeleted_idx', table_name='submissions')
    op.drop_index('submission_new_sort_idx', table_name='submissions')
    op.drop_index('submission_pinned_idx', table_name='submissions')
    op.drop_index('submissions_author_index', table_name='submissions')
    op.drop_index('submissions_created_utc_asc_idx', table_name='submissions')
    op.drop_index('submissions_created_utc_desc_idx', table_name='submissions')
    op.drop_index('submissions_over18_index', table_name='submissions')
    op.create_foreign_key(None, 'submissions', 'oauth_apps', ['app_id'], ['id'])
    op.drop_index('subs_idx', table_name='subs')
    op.drop_index('subscription_user_index', table_name='subscriptions')
    op.drop_index('block_target_idx', table_name='userblocks')
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'namecolor',
               existing_type=sa.VARCHAR(length=6),
               nullable=True)
    op.alter_column('users', 'titlecolor',
               existing_type=sa.VARCHAR(length=6),
               nullable=True)
    op.alter_column('users', 'theme',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
    op.alter_column('users', 'themecolor',
               existing_type=sa.VARCHAR(length=6),
               nullable=True)
    op.alter_column('users', 'cardview',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'patron',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'patron_utc',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'winnings',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'passhash',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'post_count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'comment_count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'received_award_count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'admin_level',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'coins_spent',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'lootboxes_bought',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'agendaposter',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'changelogsub',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'is_activated',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'over_18',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'hidevotedon',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'highlightcomments',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('users', 'slurreplacer',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('users', 'newtab',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'newtabexternal',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('users', 'reddit',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
    op.alter_column('users', 'frontsize',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('25'))
    op.alter_column('users', 'controversial',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'is_banned',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'unban_utc',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'login_nonce',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'coins',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'truecoins',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'procoins',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'is_private',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'stored_subscriber_count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'defaultsortingcomments',
               existing_type=sa.VARCHAR(length=15),
               nullable=True,
               existing_server_default=sa.text("'new'::character varying"))
    op.alter_column('users', 'defaultsorting',
               existing_type=sa.VARCHAR(length=15),
               nullable=True,
               existing_server_default=sa.text("'new'::character varying"))
    op.alter_column('users', 'defaulttime',
               existing_type=sa.VARCHAR(length=5),
               nullable=True)
    op.alter_column('users', 'is_nofollow',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'ban_evade',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'subs_created',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.drop_index('discord_id_idx', table_name='users')
    op.drop_index('fki_user_referrer_fkey', table_name='users')
    op.drop_constraint('one_banner', 'users', type_='unique')
    op.drop_constraint('one_discord_account', 'users', type_='unique')
    op.drop_constraint('uid_unique', 'users', type_='unique')
    op.drop_index('user_banned_idx', table_name='users')
    op.drop_index('user_private_idx', table_name='users')
    op.drop_index('users_created_utc_index', table_name='users')
    op.drop_constraint('users_original_username_key', 'users', type_='unique')
    op.drop_index('users_original_username_trgm_idx', table_name='users')
    op.drop_index('users_subs_idx', table_name='users')
    op.drop_index('users_unbanutc_idx', table_name='users')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_index('users_username_trgm_idx', table_name='users')
    op.alter_column('viewers', 'last_view_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('fki_view_viewer_fkey', table_name='viewers')
    op.alter_column('votes', 'vote_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('votes', 'real',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('votes', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('vote_user_index', table_name='votes')
    op.drop_index('votes_type_index', table_name='votes')
    op.create_foreign_key(None, 'votes', 'oauth_apps', ['app_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.create_index('votes_type_index', 'votes', ['vote_type'], unique=False)
    op.create_index('vote_user_index', 'votes', ['user_id'], unique=False)
    op.alter_column('votes', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('votes', 'real',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('votes', 'vote_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('fki_view_viewer_fkey', 'viewers', ['viewer_id'], unique=False)
    op.alter_column('viewers', 'last_view_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('users_username_trgm_idx', 'users', ['username'], unique=False)
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_index('users_unbanutc_idx', 'users', ['unban_utc'], unique=False)
    op.create_index('users_subs_idx', 'users', ['stored_subscriber_count'], unique=False)
    op.create_index('users_original_username_trgm_idx', 'users', ['original_username'], unique=False)
    op.create_unique_constraint('users_original_username_key', 'users', ['original_username'])
    op.create_index('users_created_utc_index', 'users', ['created_utc'], unique=False)
    op.create_index('user_private_idx', 'users', ['is_private'], unique=False)
    op.create_index('user_banned_idx', 'users', ['is_banned'], unique=False)
    op.create_unique_constraint('uid_unique', 'users', ['id'])
    op.create_unique_constraint('one_discord_account', 'users', ['discord_id'])
    op.create_unique_constraint('one_banner', 'users', ['bannerurl'])
    op.create_index('fki_user_referrer_fkey', 'users', ['referred_by'], unique=False)
    op.create_index('discord_id_idx', 'users', ['discord_id'], unique=False)
    op.alter_column('users', 'subs_created',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'ban_evade',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'is_nofollow',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'defaulttime',
               existing_type=sa.VARCHAR(length=5),
               nullable=False)
    op.alter_column('users', 'defaultsorting',
               existing_type=sa.VARCHAR(length=15),
               nullable=False,
               existing_server_default=sa.text("'new'::character varying"))
    op.alter_column('users', 'defaultsortingcomments',
               existing_type=sa.VARCHAR(length=15),
               nullable=False,
               existing_server_default=sa.text("'new'::character varying"))
    op.alter_column('users', 'stored_subscriber_count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'is_private',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'procoins',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'truecoins',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'coins',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'login_nonce',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'unban_utc',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'is_banned',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'controversial',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'frontsize',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('25'))
    op.alter_column('users', 'reddit',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)
    op.alter_column('users', 'newtabexternal',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('users', 'newtab',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'slurreplacer',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('users', 'highlightcomments',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('users', 'hidevotedon',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'over_18',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'is_activated',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'changelogsub',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('users', 'agendaposter',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'lootboxes_bought',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'coins_spent',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'admin_level',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('users', 'received_award_count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'comment_count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'post_count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'passhash',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('users', 'winnings',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'patron_utc',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'patron',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('users', 'cardview',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'themecolor',
               existing_type=sa.VARCHAR(length=6),
               nullable=False)
    op.alter_column('users', 'theme',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)
    op.alter_column('users', 'titlecolor',
               existing_type=sa.VARCHAR(length=6),
               nullable=False)
    op.alter_column('users', 'namecolor',
               existing_type=sa.VARCHAR(length=6),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_index('block_target_idx', 'userblocks', ['target_id'], unique=False)
    op.create_index('subscription_user_index', 'subscriptions', ['user_id'], unique=False)
    op.create_index('subs_idx', 'subs', ['name'], unique=False)
    op.drop_constraint(None, 'submissions', type_='foreignkey')
    op.create_index('submissions_over18_index', 'submissions', ['over_18'], unique=False)
    op.create_index('submissions_created_utc_desc_idx', 'submissions', ['created_utc'], unique=False)
    op.create_index('submissions_created_utc_asc_idx', 'submissions', ['created_utc'], unique=False)
    op.create_index('submissions_author_index', 'submissions', ['author_id'], unique=False)
    op.create_index('submission_pinned_idx', 'submissions', ['is_pinned'], unique=False)
    op.create_index('submission_new_sort_idx', 'submissions', ['is_banned', 'deleted_utc', 'created_utc', 'over_18'], unique=False)
    op.create_index('submission_isdeleted_idx', 'submissions', ['deleted_utc'], unique=False)
    op.create_index('submission_isbanned_idx', 'submissions', ['is_banned'], unique=False)
    op.create_index('subimssion_binary_group_idx', 'submissions', ['is_banned', 'deleted_utc', 'over_18'], unique=False)
    op.create_index('post_app_id_idx', 'submissions', ['app_id'], unique=False)
    op.create_index('fki_submissions_approver_fkey', 'submissions', ['is_approved'], unique=False)
    op.alter_column('submissions', 'title_html',
               existing_type=sa.VARCHAR(length=1500),
               nullable=False)
    op.alter_column('submissions', 'title',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('submissions', 'downvotes',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'upvotes',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('1'))
    op.alter_column('submissions', 'is_bot',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'over_18',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'comment_count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'club',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'private',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'is_pinned',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'distinguish_level',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'deleted_utc',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'views',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'ghost',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'is_banned',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('submissions', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('submissions', 'edited_utc',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('submissions', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('submissions', 'bump_utc')
    op.create_index('fki_sub_blocks_sub_fkey', 'sub_blocks', ['sub'], unique=False)
    op.create_index('fki_save_relationship_submission_fkey', 'save_relationship', ['submission_id'], unique=False)
    op.create_unique_constraint('unique_id', 'oauth_apps', ['client_id'])
    op.alter_column('oauth_apps', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('oauth_apps', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('oauth_apps', 'redirect_uri',
               existing_type=sa.VARCHAR(length=4096),
               nullable=False)
    op.alter_column('oauth_apps', 'app_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.create_index('notifs_user_read_idx', 'notifications', ['user_id', 'read'], unique=False)
    op.create_index('notifications_comment_idx', 'notifications', ['comment_id'], unique=False)
    op.create_index('notification_read_idx', 'notifications', ['read'], unique=False)
    op.alter_column('notifications', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('notifications', 'read',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.create_index('fki_mod_sub_fkey', 'mods', ['sub'], unique=False)
    op.alter_column('mods', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'modactions', type_='foreignkey')
    op.create_index('modaction_pid_idx', 'modactions', ['target_submission_id'], unique=False)
    op.create_index('modaction_id_idx', 'modactions', ['id'], unique=False)
    op.create_index('modaction_cid_idx', 'modactions', ['target_comment_id'], unique=False)
    op.create_index('modaction_action_idx', 'modactions', ['kind'], unique=False)
    op.create_index('fki_modactions_user_fkey', 'modactions', ['target_user_id'], unique=False)
    op.alter_column('modactions', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('marseys_idx3', 'marseys', ['count'], unique=False)
    op.create_index('marseys_idx2', 'marseys', ['author_id'], unique=False)
    op.create_index('marseys_idx', 'marseys', ['name'], unique=False)
    op.alter_column('marseys', 'count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('marseys', 'tags',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('marseys', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('follow_user_id_index', 'follows', ['user_id'], unique=False)
    op.alter_column('follows', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('flag_user_idx', 'flags', ['user_id'], unique=False)
    op.alter_column('flags', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('fki_exile_sub_fkey', 'exiles', ['sub'], unique=False)
    op.create_index('fki_exile_exiler_fkey', 'exiles', ['exiler_id'], unique=False)
    op.alter_column('exiles', 'exiler_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'commentvotes', type_='foreignkey')
    op.create_index('cvote_user_index', 'commentvotes', ['user_id'], unique=False)
    op.create_index('commentvotes_comments_type_index', 'commentvotes', ['vote_type'], unique=False)
    op.alter_column('commentvotes', 'created_utc',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('commentvotes', 'real',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('commentvotes', 'vote_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'comments', type_='foreignkey')
    # ### end Alembic commands ###
