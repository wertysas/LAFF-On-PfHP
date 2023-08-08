#define alpha( i,j ) A[ (j)*ldA + i ]   // map alpha( i,j ) to array A 
#define chi( i )  x[ (i)*incx ]         // map chi( i )  to array x
#define psi( i )  y[ (i)*incy ]         // map psi( i )  to array y

// y = alpha*x + y
void Axpy( int n, double alpha, double *x, int incx, double *y, int incy);

void MyGer( int m, int n, double *x, int incx,
		 double *y, int incy, double *A, int ldA ) {
  for ( int i=0; i<m; i++ ) 
  // arow_i = x_i*y + arow_i
    Axpy(n, x[incx*i], y, incy, &A[i], ldA);
}
