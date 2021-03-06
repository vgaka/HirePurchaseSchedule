import numpy as np
payschedule = []	

def hpbymonth(financeamount,flat_interest_perannum,tenor):
	intsallment = round(financeamount *  (1 + flat_interest_perannum /12 * tenor) / tenor,6)
	eir_PerYr = np.rate(tenor,intsallment,-financeamount,fv=0)*12# 0.1299999999
	for i in range(tenor+1):
		if i == 0:
			accuprincpay = round(float(financeamount),6)
			payschedule.append('Period,PrincPay,IntPay,installment,PrincBalance,Eir')
			payschedule.append([i, 0 ,0 ,0 , financeamount,eir_PerYr/12])
		else:
			pp = np.ppmt(eir_PerYr/12,i,tenor,-financeamount)
			ip = np.ipmt(eir_PerYr/12,i,tenor,-financeamount)
			accuprincpay = round(accuprincpay - pp,6)
			payschedule.append([i, pp, ip*1, intsallment, accuprincpay, eir_PerYr/12])
	return payschedule

if __name__ == '__main__':
	fnamt = 10000
	frate = 0.13
	ftenor = 60
	print('Program parameter {}, annum interest {}, month {}'.format(fnamt,frate,ftenor))
	print('-------------------------------------')
	paysch = hpbymonth(fnamt,frate,ftenor)
	for py in paysch:
		print(py)