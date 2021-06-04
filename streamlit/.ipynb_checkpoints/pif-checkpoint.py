import streamlit as st
import pandas as pd
import numpy as np

DATE_TIME = 'date/time'

st.title('Public Incentive Funding')


sidebar = st.sidebar.title("Panels")

select = st.sidebar.selectbox("Select",("Why", "Problem", "Mission", "Programs", "Program Voting", "Copyright"), 1)

if select == "Why":
    st.video('https://www.youtube.com/watch?v=u4ZoJKF_VuA')
    st.subheader("'People don't buy what you do, they buy why you do it.'")
    st.write("""
    ## Why 
    ### Because we have but one obligation
    May 31st Daily Stoic 
    "What is your vocation? To be a good person."
        - Marcus Aurelius, Meditations, 11.5  

    Consitent Theme behind Philosophical Ethics and all Religions is to be good people in 
    their own way.  PIF Corp exists because it is our obligation and vocation to be Good People.
    Good People treat all people with respect.  Good People train their skills to become better than most in their field; Being Good at your Job.
    Good People work hard to augment their skills to monetize their abilities.  They provide for their family and 
    give back to the community. WHY does PIF Corp exist? Because we believe that it is our 
    single true obligation in this life: to be a good person. Because we believe that YOU are inherently Good People.  
    """)


if select == "Problem":    
    st.write("""
    ## Problem
    - Access to Education
    
    ## How are people trying to solve this problem?
    - Charter Schools: Red Bank Charter School, Success Academy, KIPP, Classical, Ascend
    - Free Educational Resources such as Code Academy, 3 Blue 1 Brown, 
    """)
    
    

    st.image("/Users/wesleysapone/PIF/public_incentive_funding/images/law_diffusion_innovation.png")

if select == "Mission":
    
    st.write("""
    ## PIF
    ### Mission: To fund public innovation and education through efficient allocation programs and activities.
    ### Vision: To cultivate a better future by increasing access to educational resources.  To encourage the public to learn more.""")

    
if select == "Programs":
    st.write("""## Program Directory""")
    if st.checkbox("Tech Resources for Red Bank Charter School"):
        st.subheader("Addresses: ")
        st.write("ETH: ")
        st.write("BTC: 36o2gsxQuZ9eLppHNEyFts8AWX8PRiuRA3")
        st.write("DAI: ")
    
    if st.checkbox("Financial Literacy at Red Bank Charter School"):
        st.subheader("Addresses: ")
        st.write("ETH: ")
        st.write("BTC: 3PkW2biWqEvG24rWgjzPpJUwPz66qQtFnc")
        st.write("DAI: ")
        
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
        
if select == "Copyright":
    st.subheader("Copyright your PIF Program")