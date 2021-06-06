import streamlit as st
import pandas as pd
import numpy as np

DATE_TIME = 'date/time'
st.title("PIF Corp.")
st.header('Public Incentive Funding')
st.write("Building Pipelines of Funding for Charitable Incentives")

sidebar = st.sidebar.title("Panels")

select = st.sidebar.selectbox("Select",("Why", "Problem", "Mission", "Programs", "Program Voting", "Crowdsale Contract", "Escrow", "Future Considerations", "Trouble shooting"), 1)

if select == "Why":
    if st.checkbox("What's your why?"):
        st.video('https://www.youtube.com/watch?v=u4ZoJKF_VuA')
    st.subheader("'People don't buy what you do, they buy why you do it.'")
    st.write("""
    ## Why 
    ### Because we have but one obligation
    
    "What is your vocation? To be a good person."
        - Marcus Aurelius, Meditations, 11.5  

    Consitent Theme behind Philosophical Ethics and all World Religions: they all teach us how to be Good People.  PIF Corp exists because it is our obligation and vocation to be Good People.
    
    Good People treat the world with respect: the soil we grow our food with, the air we breathe, the water we quench our thirst with and the people whom we share God's gifts with.  

    Good People are good at their job. Good People provide for their family and give back to the community. 
    
    WHY does PIF Corp exist? Because we believe that it is our single true obligation in this life: to be a good person. 
    
    Because we believe that YOU are inherently Good People.  We believe that we can make a significant impact one PIF programmer at a time.  
    """)
    
    st.write("""
    Blockchains exist to solve problems, serve as a network, as a database and as a computer.  
    We are building the worlds first public sector organization on the blockchain because we aren't trying to solve just another problem.  We are going to solve THE problem.
    
    Blockchains' public ledgers will allow funders' impact to be tracked, quantified and audited.  
    Our Learn by doing content will encourage funders' to improve themselves, inspire people around themselves to improve.  Inspire people around them to support causes that they believe in.

    We believe that a rising tide lifts all boats.  We believe that you have the gaul and gunction to improve yourself, inspire people and lift people up.
    Join us on this journey to educate and innovate for the benefit of our future.  
    """)

if select == "Problem":    
    st.write("""
    ## THE Problem
    - Public access to Educational, Athletic and Healthy resources
    - Under-funded and under-utilized Charter Schools
    - Vicious cycle of poverty  
    """)
    st.image("https://societyhealth.vcu.edu/media/society-health/projects/ehi2/Model-RGB-web.gif")
    st.write("""
    ## How are people trying to solve this problem?
    - Charter Schools: Red Bank Charter School, Success Academy, KIPP, Classical, Ascend
    - Free Educational Resources such as Code Academy, 3 Blue 1 Brown, Khan Academy, YouTube

    ## How our solution is unique and will add value 
    - Blockchain for tracking, transparency, and consensus mechanisms
    - Restricted and Unrestricted programs: funding will go 100% toward what funders wish
    - Fostering collaboration and finding synergies between educational 501(c)3 organizations and free resources
    - Learn By Doing content: public educational resources tailored to our users
    - Learn By Teaching Peer to Peer tutor network
    - Additional payment options: Venmo and Zelle for now; working to incorporate a gateway. 
    
    ## Value Adds of blockchain
    
    - open system : everyone owns their own data, not the bank.  information is immutable 
    - tustless : controlled by individuals, with a set of rules set by computers that cant be changed.  Every computer gets a copy of the public ledger. All of our donations will be able to be tracked by the public. 
    - Public network : anyone can access the network all you need is internet connection.
    """)
    st.image("/Users/wesleysapone/PIF/public_incentive_funding/images/Untitled 2.png")
    st.write("""
    - Database : because it stores information on it.  Nonprofits* currently pay tons of money for CRM software systems.  The blockchain only charges gas fees.
    - Computer : each address is equivalent to a node.  nodes are like redundant web servers.  
    - consensus mechanism : not reachd, transaction isn't recorded
    """)
    st.image("/Users/wesleysapone/PIF/public_incentive_funding/images/byzant.png")
if select == "Mission":
    
    st.write("""
    ### Mission: To fund public innovation and education through efficient allocation programs and activities.
    ### Vision: To cultivate a better future by increasing access to educational resources.  To encourage the public to learn more.""")
    st.subheader("How")
    
    st.write("1. Open Addresses for each program we support")
    
    link = '[RBCS](http://www.redbankcharterschool.com/rbcs/Foundation/)'
    st.markdown(link, unsafe_allow_html=True)
    st.write("""
    Our pilot programs will help fund the gymnasium and supplying students with necessary technology resources at Red Bank Charter School.  """)

    st.write("""
    2. Sweep each program's balance quarterly
    """)
    st.write("""We will write into the Ecrow contract to sweep the balance quarterly to the program's fiat gateway so that they can purchase resources or contribute towards a fundraiser like the one for the gymnasium.
    """)

    st.write("3. Track the impact that each program made")
    st.write("""
    There will be visualizations of the impacts raised.  We hope to incorporate a color scheme that interacts with the addresses that support each program the most.  

    
    """)

    
if select == "Programs":
    st.write("""## Program Directory""")
    if st.checkbox("Tech Resources for Red Bank Charter School"):
        st.write("Addresses: ")
        st.write("ETH: 0x8AB11B8A29A428B3C2F8fD263C781105Efc9e8b2")
        link2 = '[Transactions](https://etherscan.io/address/0x8AB11B8A29A428B3C2F8fD263C781105Efc9e8b2)'
        st.markdown(link2, unsafe_allow_html=True)
        
        st.write("BTC: 36o2gsxQuZ9eLppHNEyFts8AWX8PRiuRA3")
        # st.write("DAI: ")
    
    if st.checkbox("Gymnasium at Red Bank Charter School"):
        st.write("Addresses: ")
        st.write("ETH: 0x97c977f374d218aEFFafCB3aDdBd3DAA0E69a766")
        link3 = '[Transactions](https://etherscan.io/address/0x97c977f374d218aEFFafCB3aDdBd3DAA0E69a766)'
        st.markdown(link3, unsafe_allow_html=True)
        st.write("BTC: 3PkW2biWqEvG24rWgjzPpJUwPz66qQtFnc")
        # st.write("DAI: ")
        
if select == "Program Voting":
        st.subheader("Become a PIF Programmer")
        
        code = '''
       pragma solidity 0.4.25;

       contract Election {
            // Model a Candidate
            struct Candidate {
                uint id;
                string name;
                uint voteCount;
            }

            // Store accounts that have voted
            mapping(address => bool) public voters;
            // Store Candidates
            // Fetch Candidate
            mapping(uint => Candidate) public candidates;
            // Store Candidates Count
            uint public candidatesCount;

            // voted event
            event votedEvent (
                uint indexed _candidateId
            );

            constructor () public {
                addCandidate("Candidate 1");
                addCandidate("Candidate 2");
            }

            function addCandidate (string _name) private {
                candidatesCount ++;
                candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
            }

            function vote (uint _candidateId) public {
                // require that they haven't voted before
                require(!voters[msg.sender]);

                // require a valid candidate
                require(_candidateId > 0 && _candidateId <= candidatesCount);

                // record that voter has voted
                voters[msg.sender] = true;

                // update candidate vote Count
                candidates[_candidateId].voteCount ++;

                // trigger voted event
                emit votedEvent(_candidateId);
            }
        }'''
        st.code(code, language='solidity')      
        
        video_file = open('election_demo.gif', 'rb')
        
if select == "Crowdsale Contract":
        st.subheader("Copyright your PIF Program")
        st.write("""
        After an incentive program is voted in and we want to start raising funds for it, we create a crowdsale contract. 
        This crowdsale contract manages the entire process, allowing users to send ETH and get back PIFCoin (Public Incentive Funding Coin).

        This contract will mint the tokens automatically and distribute them to buyers in one transaction.
        
        The crowdsale contract will inherit from:

        1.  Crowdsale - takes in rate, wallet, and token as parameters
        2. CappedCrowdsale - takes in goal as a parameter
        3. TimedCrowdsale - takes in openingTime and closingTime as parameters
        4. RefundableCrowdsale - takes in goal as a parameter
        5. MintedCrowdsale
        These customizable parameters will change depending on the Incentive in question.
        """)
        
if select == "Escrow":
    code_2 = '''
    pragma solidity ^0.6.0;

    contract Escrow {
        enum State { AWAITING_PAYMENT, AWAITING_DELIVERY, COMPLETE }
    
        State public currentState;
    
        address public buyer;
        address payable public seller;
    
        modifier onlyBuyer() {
            require(msg.sender == buyer, "Only buyer can call this method");
            _;
        }
    
        constructor(address _buyer, address payable _seller) public {
            buyer = _buyer;
            seller = _seller;
        }
    
        function deposit() onlyBuyer external payable {
            require(currentState == State.AWAITING_PAYMENT, "Already paid");
            currentState = State.AWAITING_DELIVERY;
        }
    
        function confirmDelivery() onlyBuyer external {
            require(currentState == State.AWAITING_DELIVERY, "Cannot confirm delivery");
            seller.transfer(address(this).balance);
            currentState = State.COMPLETE;
        }
    }'''

    st.code(code_2, language='solidity')
    st.write("""
    This is a simple escrow contract that we will use to sweep funds to charities.
    """)
    st.write("""
    The goal is to encourage charities to set up payment gateways on Meta Mask so that we can swepp funds more easily.  

    We would like to move towards USDC and USDT to reduce the volitility of our assets.  Although the assets are not really ours and price increases of ETH and BTC would make tracking more difficult.  WE would like to create a Staking pool within the next year.  
    """)
    

if select == "Future Considerations":
    st.subheader("NFT marketplace")
    auction_code = '''
pragma solidity ^0.5.0;

contract Auction {
    // static
    address public owner;
    uint public bidIncrement;
    uint public startBlock;
    uint public endBlock;
    string public ipfsHash;

    // state
    bool public canceled;
    uint public highestBindingBid;
    address public highestBidder;
    mapping(address => uint256) public fundsByBidder;
    bool ownerHasWithdrawn;

    event LogBid(address bidder, uint bid, address highestBidder, uint highestBid, uint highestBindingBid);
    event LogWithdrawal(address withdrawer, address withdrawalAccount, uint amount);
    event LogCanceled();

    function Auction(address _owner, uint _bidIncrement, uint _startBlock, uint _endBlock, string _ipfsHash) {
        if (_startBlock >= _endBlock) throw;
        if (_startBlock < block.number) throw;
        if (_owner == 0) throw;

        owner = _owner;
        bidIncrement = _bidIncrement;
        startBlock = _startBlock;
        endBlock = _endBlock;
        ipfsHash = _ipfsHash;
    }

    function getHighestBid()
        constant
        returns (uint)
    {
        return fundsByBidder[highestBidder];
    }

    function placeBid()
        payable
        onlyAfterStart
        onlyBeforeEnd
        onlyNotCanceled
        onlyNotOwner
        returns (bool success)
    {
        // reject payments of 0 ETH
        if (msg.value == 0) throw;

        // calculate the user's total bid based on the current amount they've sent to the contract
        // plus whatever has been sent with this transaction
        uint newBid = fundsByBidder[msg.sender] + msg.value;

        // if the user isn't even willing to overbid the highest binding bid, there's nothing for us
        // to do except revert the transaction.
        if (newBid <= highestBindingBid) throw;

        // grab the previous highest bid (before updating fundsByBidder, in case msg.sender is the
        // highestBidder and is just increasing their maximum bid).
        uint highestBid = fundsByBidder[highestBidder];

        fundsByBidder[msg.sender] = newBid;

        if (newBid <= highestBid) {
            // if the user has overbid the highestBindingBid but not the highestBid, we simply
            // increase the highestBindingBid and leave highestBidder alone.

            // note that this case is impossible if msg.sender == highestBidder because you can never
            // bid less ETH than you've already bid.

            highestBindingBid = min(newBid + bidIncrement, highestBid);
        } else {
            // if msg.sender is already the highest bidder, they must simply be wanting to raise
            // their maximum bid, in which case we shouldn't increase the highestBindingBid.

            // if the user is NOT highestBidder, and has overbid highestBid completely, we set them
            // as the new highestBidder and recalculate highestBindingBid.

            if (msg.sender != highestBidder) {
                highestBidder = msg.sender;
                highestBindingBid = min(newBid, highestBid + bidIncrement);
            }
            highestBid = newBid;
        }

        LogBid(msg.sender, newBid, highestBidder, highestBid, highestBindingBid);
        return true;
    }

    function min(uint a, uint b)
        private
        constant
        returns (uint)
    {
        if (a < b) return a;
        return b;
    }

    function cancelAuction()
        onlyOwner
        onlyBeforeEnd
        onlyNotCanceled
        returns (bool success)
    {
        canceled = true;
        LogCanceled();
        return true;
    }

    function withdraw()
        onlyEndedOrCanceled
        returns (bool success)
    {
        address withdrawalAccount;
        uint withdrawalAmount;

        if (canceled) {
            // if the auction was canceled, everyone should simply be allowed to withdraw their funds
            withdrawalAccount = msg.sender;
            withdrawalAmount = fundsByBidder[withdrawalAccount];

        } else {
            // the auction finished without being canceled

            if (msg.sender == owner) {
                // the auction's owner should be allowed to withdraw the highestBindingBid
                withdrawalAccount = highestBidder;
                withdrawalAmount = highestBindingBid;
                ownerHasWithdrawn = true;

            } else if (msg.sender == highestBidder) {
                // the highest bidder should only be allowed to withdraw the difference between their
                // highest bid and the highestBindingBid
                withdrawalAccount = highestBidder;
                if (ownerHasWithdrawn) {
                    withdrawalAmount = fundsByBidder[highestBidder];
                } else {
                    withdrawalAmount = fundsByBidder[highestBidder] - highestBindingBid;
                }

            } else {
                // anyone who participated but did not win the auction should be allowed to withdraw
                // the full amount of their funds
                withdrawalAccount = msg.sender;
                withdrawalAmount = fundsByBidder[withdrawalAccount];
            }
        }

        if (withdrawalAmount == 0) throw;

        fundsByBidder[withdrawalAccount] -= withdrawalAmount;

        // send the funds
        if (!msg.sender.send(withdrawalAmount)) throw;

        LogWithdrawal(msg.sender, withdrawalAccount, withdrawalAmount);

        return true;
    }

    modifier onlyOwner {
        if (msg.sender != owner) throw;
        _;
    }

    modifier onlyNotOwner {
        if (msg.sender == owner) throw;
        _;
    }

    modifier onlyAfterStart {
        if (block.number < startBlock) throw;
        _;
    }

    modifier onlyBeforeEnd {
        if (block.number > endBlock) throw;
        _;
    }

    modifier onlyNotCanceled {
        if (canceled) throw;
        _;
    }

    modifier onlyEndedOrCanceled {
        if (block.number < endBlock && !canceled) throw;
        _;
    }
}'''
    st.code(auction_code, language='solidity')
    st.write("""
    We will have students create art and then we will tokenize the art and contribute the proceeds from the auction to the programs that the students are a part of.

    It could be a specific program at a charter school or an unrestircted donation to the charter school the student attends. 
    
    """)
    st.subheader("Micro-grants")
    st.write("""
    This is one of the main methods or activities that I would like to incorporate.  

    We will offer micro grants to affordable bootcamps and paid educational resources on our website.  Students can apply and if they meet the criteria defined by smart contracts, then they will be approved and the stable coin will be sent to an address for that student and that student will direct the funds toward a bootcamp or extra-curricular class.
    
    This is inspried by Mohammed Yunus's micro-lending model

    instead of having groups of lenders though, we will have groups of students that hold eachother accountable. 

    """)
if select == "Trouble shooting":
    st.write("""
    - M1 chip compatibility 
    - Front-end issues
    - few PIF programmers
    - new to software engineering
    - full time jobs 
    """)