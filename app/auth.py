"""
auth.py
-------
Authentication module for Curriculum Gap Analyzer.
Handles user signup, login, and session management using Supabase.

Author: Parth Koli
College: Satish Pradhan Dnyanasadhana College, Thane
Project: Curriculum Gap Analyzer (Final Year Project 2026-27)
"""

import bcrypt
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def init_db():
    """No-op for Supabase — tables already created in dashboard"""
    pass

def signup_user(username, email, password, college=""):
    """Register a new user"""
    try:
        supabase = get_client()
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Check if username exists
        existing = supabase.table('users').select('id').eq('username', username).execute()
        if existing.data:
            return False, "Username already exists!"
        
        # Check if email exists
        existing_email = supabase.table('users').select('id').eq('email', email).execute()
        if existing_email.data:
            return False, "Email already exists!"
        
        # Insert new user
        supabase.table('users').insert({
            'username': username,
            'email': email,
            'password': hashed,
            'college': college
        }).execute()
        
        return True, "Account created successfully!"
    except Exception as e:
        return False, str(e)

def login_user(username, password):
    """Authenticate a user"""
    try:
        supabase = get_client()
        result = supabase.table('users').select('id, username, password, college').eq('username', username).execute()
        
        if not result.data:
            return False, "Invalid username or password!"
        
        user = result.data[0]
        if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return True, {"id": user['id'], "username": user['username'], "college": user['college']}
        
        return False, "Invalid username or password!"
    except Exception as e:
        return False, str(e)

def save_report(user_id, report_name, coverage_pct, gaps_found, skills_covered):
    """Save a gap analysis report for a user"""
    try:
        supabase = get_client()
        supabase.table('saved_reports').insert({
            'user_id': user_id,
            'report_name': report_name,
            'coverage_pct': coverage_pct,
            'gaps_found': gaps_found,
            'skills_covered': skills_covered
        }).execute()
        return True
    except Exception as e:
        print(f"Error saving report: {e}")
        return False

def get_user_reports(user_id):
    """Get all saved reports for a user"""
    try:
        supabase = get_client()
        result = supabase.table('saved_reports').select(
            'report_name, coverage_pct, gaps_found, skills_covered, created_at'
        ).eq('user_id', user_id).order('created_at', desc=True).execute()
        
        # Convert to list of tuples to match existing code
        reports = [
            (r['report_name'], r['coverage_pct'], r['gaps_found'], 
             r['skills_covered'], r['created_at'])
            for r in result.data
        ]
        return reports
    except Exception as e:
        print(f"Error fetching reports: {e}")
        return []