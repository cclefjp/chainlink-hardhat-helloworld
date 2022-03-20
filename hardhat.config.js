
require("@nomiclabs/hardhat-waffle");

/*
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.8.7",

  networks: {
    hardhat: {

    },
    kovan: {
      url: process.env.KOVAN_URL,
      accounts: [process.env.KOVAN_KEY]
    }
  }
};
