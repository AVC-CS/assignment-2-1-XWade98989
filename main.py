def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m = int(input("How many males in the class?"))
    f = int(input("How many females in the class?"))

    total = m + f
    m_perc = m/total * 100
    f_perc = f/total * 100
    print("total number of students is:", total)
    print(f'The percentage of males is \t {m_perc:.2f}')
    print(f'The percentage of females is \t {f_perc:.2f}')


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
