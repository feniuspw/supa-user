import os
import sys
import types

# Ensure environment variables used by the application exist
os.environ.setdefault("SUPABASE_URL", "http://test")
os.environ.setdefault("SUPABASE_API_KEY", "test-key")
os.environ.setdefault("SSO_REDIRECT_TO", "http://localhost")

# Add src directory to Python path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Provide a dummy supabase module if the real one is unavailable
if "supabase" not in sys.modules:
    supabase = types.ModuleType("supabase")
    supabase.create_client = lambda url, key: types.SimpleNamespace(auth={})
    sys.modules["supabase"] = supabase
