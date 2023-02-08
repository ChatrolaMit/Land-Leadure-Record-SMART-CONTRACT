// SPDX-Licence-Identifier : MIT 

pragma solidity ^0.6.6 ;

// import "./land_record.sol";
// import "./upin_to_address.sol";

contract Peoples  {
    string [] public peoples;
    mapping(string => address ) public people_to_upin;
    // LandRecord public 
    
    // constructor (string memory _f_id, address _f_address ) public {
    //     peoples.push(_f_id);
    //     people_to_upin[_f_id] = _f_address ;
    // }
    function add_people(string memory _f_id, address _f_address ) public {
        peoples.push(_f_id);
        people_to_upin[_f_id] = _f_address ;
    }
}