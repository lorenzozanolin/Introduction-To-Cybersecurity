//given function
bool match ( char * C , char * P ,int Clen ,int Plen )
{
    bool value = true ;
    if ( Clen != Plen ) { value = false ; }
    for (int i =0; i < Plen && value == true ; i ++)
    {
    if ( C [ i ] != P [ i ] ) { value = false ; }
    }
    return value ;
}

//alternatives

//1.
bool match ( char * C , char * P ,int Clen ,int Plen )
{
    bool value = false;
    if ( Clen == Plen ) 
    { 
        //the only possible attack is to skip the for entirely by exploiting power to skip instructions.
        for (int i =0; i < Plen; i ++)
        {
            if ( C [ i ] != P [ i ] ) { return; }
        }
        value = true;
    }
    return value ;
}

//2.
bool match ( char * C , char * P ,int Clen ,int Plen )
{
    if ( Clen != Plen ) { return false ; }
    for (int i =0; i < Plen; i ++)
    {
        if ( C [ i ] != P [ i ] ) { return false ; }
        if (i==Plen-1){return true;}
    }
    return false;
}
//very similar to the one example given, you can skip over the for instruction

