# User Configurable Parameters for Tourbillon Bot

params = {
    "asset": "BTC",
    "side": "buy",
    # --- License Configuration ---
    # Replace with the user's Stripe Subscription ID
    "license_key": "YOUR_LICENSE_KEY_HERE",
    # Note: 'license_key' is now used for the Stripe Subscription ID

    # --- Trading Parameters ---
    "position_size": 0.005,
    "num_orders": 6,
    "spacing_percentage": 0.76,
    "spacing_multiplier": 1.33,  # Each level's spacing will be x the previous >1 recommended
    "size_multiplier": 0.8,     # Each level's size will be x the previous <1 recommended
    "leverage": 20,
    "initial_offset_percentage": 0.6,  # Start the grid 3% away from current price
    "constant_offset_percentage": 0.55,  # Smaller offset for subsequent cycles
    "orderblocktrigger": True,  # If True, use initial_offset only on first cycle
    # Take profit parameters
    "num_orderstp": 6,
    "tp_size": 0.0015,
    "tp_spacing_percentage": 0.20,
    "cancel_tp": False,  # New parameter to control TP order cancellation
    "duplicate_tporders": False,  # New parameter to control duplicate TP orders
    "num_orderstpmatch": True,  # New parameter to enforce TP order quantity matching
    "tp_initialize": True,  # New parameter to enable dynamic TP order initialization
    # Cycle control parameters
    "cycle_endfunction": False,  # New parameter to control cycle-based termination
    "cycle_duration": 50,  # New parameter for maximum number of cycles
    "enable_staticorder": True,  # Enable/disable waiting for price movement before cycle timer
    "grid_repeatthreshold": 4.0,  # Percentage price movement needed to trigger next cycle
    "grid_shift": True,  # Enable bidirectional cycle triggering based on price movement
    "reset_cycle_at_zero": True,  # Enable resetting cycle when no position for specified hours
    "RCAZ_timer": 24,  # Hours to wait with no position before resetting cycle (default: 12)
    # Derisk control parameters
    "derisk_control": True,  # Enable/disable derisk control functionality
    "maxsize_threshold": 0.04,  # Maximum position size threshold
    "derisk_tp": -0.15,  # Take profit percentage for derisk order
    # Trade side constant parameters
    "trade_side_constant": True,  # Enable/disable trade side constant monitoring
    # Stop loss parameters (Added back with default False)
    "stop_loss": False,
    "sl_percentage": 15.0,
    # Profit lock parameters (Added back with default False)
    "profit_lock": False,
    "tp_threshold": 1.0,
    "trailing_profit": 0.35,
    # Secondary take profit grid parameters (Added back with default False)
    "secondary_tp": False,
    "secondary_spacing_percentage": 0.15,
    "secondary_num_orderstp": 4,
    "secondary_tp_size": 0.01,
}
