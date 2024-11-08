-- schema.sql
-- Users table to store Discord user information
CREATE TABLE
    IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        username TEXT NOT NULL
    );

-- Streaks table to store win streaks between players
CREATE TABLE
    IF NOT EXISTS streaks (
        streak_id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id BIGINT NOT NULL,
        opponent_id BIGINT NOT NULL,
        streak_count INTEGER NOT NULL,
        date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (player_id) REFERENCES users (user_id),
        FOREIGN KEY (opponent_id) REFERENCES users (user_id),
        UNIQUE (player_id, opponent_id)
    );

-- Create indexes for faster lookups
CREATE INDEX IF NOT EXISTS idx_streaks_player ON streaks (player_id);
CREATE INDEX IF NOT EXISTS idx_streaks_opponent ON streaks (opponent_id);