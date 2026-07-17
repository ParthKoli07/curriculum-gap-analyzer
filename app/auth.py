"""
auth.py
-------
Authentication module for Curriculum Gap Analyzer.
Handles user signup, login, and session management using SQLite.

Author: Parth Koli
College: Satish Pradhan Dnyanasadhana College, Thane
Project: Curriculum Gap Analyzer (Final Year Project 2026-27)
"""

import sqlite3
import bcrypt
import os

DB_PATH = "data/users.db"

def init_db():
    """Initialize the SQLite database and create users table"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            college TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS saved_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            report_name TEXT,
            coverage_pct REAL,
            gaps_found INTEGER,
            skills_covered INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def signup_user(username, email, password, college=""):
    """Register a new user"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        c.execute(
            "INSERT INTO users (username, email, password, college) VALUES (?, ?, ?, ?)",
            (username, email, hashed, college)
        )
        conn.commit()
        conn.close()
        return True, "Account created successfully!"
    except sqlite3.IntegrityError:
        return False, "Username or email already exists!"
    except Exception as e:
        return False, str(e)

def login_user(username, password):
    """Authenticate a user"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, username, password, college FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
            return True, {"id": user[0], "username": user[1], "college": user[3]}
        return False, "Invalid username or password!"
    except Exception as e:
        return False, str(e)

def save_report(user_id, report_name, coverage_pct, gaps_found, skills_covered):
    """Save a gap analysis report for a user"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "INSERT INTO saved_reports (user_id, report_name, coverage_pct, gaps_found, skills_covered) VALUES (?, ?, ?, ?, ?)",
            (user_id, report_name, coverage_pct, gaps_found, skills_covered)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def get_user_reports(user_id):
    """Get all saved reports for a user"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT report_name, coverage_pct, gaps_found, skills_covered, created_at FROM saved_reports WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    reports = c.fetchall()
    conn.close()
    return reports