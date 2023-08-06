#define alpha( i,j ) A[ (j)*ldA + i ]   // map alpha( i,j ) to array A 
#define chi( i )  x[ (i)*incx ]         // map chi( i )  to array x
#define psi( i )  y[ (i)*incy ]         // map psi( i )  to array y

void Dots( int n, const double *x, int incx, const double *y, int incy, double *gamma);

void MyGemv( int m, int n, double *A, int ldA,
           double *x, int incx, double *y, int incy )
{
// row vector i of A is given by A[i + ldA*j], j=0,...,n-1
  for ( int i=0; i<m; i++ )
    Dots( n, &A[i], ldA, x, incx, &y[i]);
}
