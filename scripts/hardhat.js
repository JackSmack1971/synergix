// Keep Hardhat's Windows config/data/cache directories inside this checkout.
// This also avoids failures when the roaming profile is unavailable or malformed.
const path = require("path");

const localHardhatHome = path.resolve(__dirname, "..", ".hardhat-user");
process.env.APPDATA = path.join(localHardhatHome, "Roaming");
process.env.LOCALAPPDATA = path.join(localHardhatHome, "Local");

require("hardhat/internal/cli/cli");
