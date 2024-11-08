import aiosqlite

class DatabaseManager:
    def __init__(self, *, connection: aiosqlite.Connection) -> None: 
        self.connection = connection
        
    async def register_streak(self, player_id: int, opponent_id: int, streak_count: int):
        await self.connection.execute('''
            INSERT INTO streaks (player_id, opponent_id, streak_count)
            VALUES (?, ?, ?)
            ON CONFLICT (player_id, opponent_id)
            DO UPDATE SET streak_count = ?, date_achieved = CURRENT_TIMESTAMP
        ''', (player_id, opponent_id, streak_count, streak_count))
        await self.connection.commit()
        
    async def get_all_streaks(self, player_id: int):
        async with self.connection.execute('''
            SELECT s.streak_count, u.username, s.date_achieved
            FROM streaks s
            JOIN users u ON s.opponent_id = u.user_id
            WHERE s.player_id = ?
            ORDER BY s.streak_count DESC
        ''', (player_id,)) as cursor:
            return await cursor.fetchall()